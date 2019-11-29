// Pass the results from a single query into a function
function execute(sql, callback) {
    $.post(
        "query.php",
        {query: sql},
        function(result) { callback(result); }
    );
}

// Pass the results of two separate queries into a function
function executeCombine(sql1, sql2, callback) {
    $.post(
        "query.php",
        {query: sql1},
        function(result1) {
            $.post(
                "query.php",
                {query: sql2},
                function(result2) {
                    callback(result1, result2);
                }
            );
        }
    );
}

// Allows nodes to be dragged in the 'Social Graph'
function drag(simulation) {

    function dragstarted(d) {
        if (!d3.event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }
  
    function dragged(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }
  
    function dragended(d) {
        if (!d3.event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
  
    return d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);

}

// Shows a node's information in the sidebar
function openSocialSidebar(d) {

    console.log(d);

    $("#sgs-avatar").attr("src", d.AvatarUrl);
    $("#sgs-name").text(d.Username);
    $("#sgs-bio").html((d.Bio == null) ? "<i>No bio.</i>" : d.Bio);
    $("#sgs-profileurl").attr("href", d.Url);
    $("#sgs-f1count").text(d.FollowerCount);
    $("#sgs-f2count").text(d.FollowingCount);
    $("#sgs-rcount").text(d.RepositoryCount);

    $("#social-graph-sidebar").width("360px");
    $("#social-graph").css("margin-right", "360px");

}

// Closes the sidebar
function closeSocialSidebar() {

    $("#social-graph-sidebar").width("0px");
    $("#social-graph").css("margin-right", "0px");

}

// Handle any click that isn't on a node or the sidebar
$(document).click(function(e) {
    if (($(e.target).closest("circle").length === 0) && ($(e.target).closest("#social-graph-sidebar").length === 0)) {
        closeSocialSidebar();
    }
});

// Create the 'Social Graph'
function socialGraph(dataNodes, dataLinks) {

    // convert some strings to numbers
    dataLinks.forEach(function(d) {
        d.source = +d.source;
        d.target = +d.target;
    });
    dataNodes.forEach(function(d) {
        d.Connectivity = +d.Connectivity;
    })

    var minConnectivity = d3.min(dataNodes, function(d) { return d.Connectivity; });
    var maxConnectivity = d3.max(dataNodes, function(d) { return d.Connectivity; });
    
    var interpolate = function(v, range) {
        return range[0] + ((range[1] - range[0]) * ((v + 0.0) / (maxConnectivity - minConnectivity)));
    };

    var radiusRange = [8, 26];
    var radius = function (c) { return interpolate(c, radiusRange); };
    var colorRange = [0, 1];
    var color = function (c) { return d3.interpolateYlOrRd(interpolate(c, colorRange)); };
    var strengthRange = [100, 200];
    var strength = function(c) { return -interpolate(c, strengthRange); };

    $("social-graph").css("top", $("#navbar").height() + "px");
    $("social-graph").height($(window).height() - $("#navbar").height());
    $("social-graph-sidebar").css("top", $("#navbar").height() + "px");
    $("social-graph-sidebar").height($(window).height() - $("#navbar").height());

    var margin = {top: 0, right: 0, bottom: 0, left: 0};
    var width = $("#social-graph").width();
    var height = $("#social-graph").height();

    var simulation = d3.forceSimulation(dataNodes)
        .force("link", d3.forceLink(dataLinks).id(d => d.Id))
        .force("charge", d3.forceManyBody().strength(function(d, i) { return strength(d.Connectivity); }))
        .force("center", d3.forceCenter(width / 2, height / 3));

    var svg = d3.select("#social-graph").append("svg").attr("viewBox", [0, 0, width, height]);
    
    var link = svg.append("g")
        .attr("stroke", "#BBB")
        .attr("stroke-opacity", 0.5)
        .selectAll("line")
        .data(dataLinks)
        .join("line")
        .attr("stroke-width", 1.0);
    
    var node = svg.append("g")
        .attr("stroke", "#fff")
        .attr("stroke-width", 1.5)
        .selectAll("circle")
        .data(dataNodes)
        .join("circle")
        .attr("r", function(d) { return radius(d.Connectivity); })
        .attr("fill",  function(d) { return color(d.Connectivity); })
        .call(drag(simulation))
        .on("click", openSocialSidebar);

    node.append("title").text(d => `Username: ${d.Username} \nConnections: ${d.Connectivity}`);

    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);
          node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);
    });

}

// Update the crawler stats
function setCrawlerStats(data) {
    $("#crawler-stats").html(`
        <table class="table table-sm table-borderless">
            <tbody>
                <tr>
                    <td>Queries Made:</td>
                    <td><code>${data[0].Queries}</code></td>
                </tr>
                <tr>
                    <td>Users Indexed:</td>
                    <td><code>${data[0].UsersIndexed}</code></td>
                </tr>
                <tr>
                    <td>Users Explored:</td>
                    <td><code>${data[0].UsersExplored}</code></td>
                </tr>
                <tr>
                    <td>Repos Indexed:</td>
                    <td><code>${data[0].ReposIndexed}</code></td>
                </tr>
                <tr>
                    <td>Repos Explored:</td>
                    <td><code>${data[0].ReposExplored}</code></td>
                </tr>
                <tr>
                    <td>Last Crawled:</td>
                    <td><code>${data[0].LastCrawled}</code></td>
                </tr>
            </tbody>
        </table>
    `);
}


/*function buildSelect(data) {

    var sel = $("#commit-chart-form");
    $(data).each(function() {
        sel.append($("<option>").attr("value", this.Username).text(this.Username));
    });

}*/


function init() {

    $("svg").remove();

    //execute("select * from CommitChart_SelectList", buildSelect);
    execute("select * from Overview_Stats", setCrawlerStats);
    executeCombine("select * from SocialGraph_Nodes", "select * from SocialGraph_Links", socialGraph);

}

$(window).resize(function() { init(); }); // recreate graphs on resize
init(); // initial creation of graphs
