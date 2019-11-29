function execute(sql, callback) {
    $.post(
        "query.php",
        {query: sql},
        function(result) { callback(result); }
    );
}

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

function mostPopularUsers(data, none) {

    var margin = {top: 10, right: 30, bottom: 30, left: 60};
    var width = 460 - margin.left - margin.right;
    var height = 450 - margin.top - margin.bottom;

    var svg = d3.select("#most-popular-users")
                .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    
    var x = d3.scaleLinear().domain([0, 100]).range([0, width]);
    svg.append("g").attr("transform", "translate(0," + height + ")").call(d3.axisBottom(x));

    var y = d3.scaleLinear().domain([0, 100]).range([height, 0]);
    svg.append("g") .call(d3.axisLeft(y));

    var tooltip = d3.select("#most-popular-users")
                    .append("div")
                    .style("opacity", 0)
                    .attr("class", "tooltip")
                    .style("background-color", "white")
                    .style("border", "solid")
                    .style("border-width", "1px")
                    .style("border-radius", "5px")
                    .style("padding", "10px")

    var mouseover = function(d) { tooltip.style("opacity", 1) }
    var mousemove = function(d) {
        tooltip
            .html(d.Username)
            .style("left", (d3.mouse(this)[0]+90) + "px")
            .style("top", (d3.mouse(this)[1]) + "px")
      }

    var mouseleave = function(d) {
      tooltip
        .transition()
        .duration(200)
        .style("opacity", 0)
    }

    svg.append('g')
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", function (d) { return x(d.Followers); } )
        .attr("cy", function (d) { return y(d.Stars); } )
        .attr("r", 7)
        .style("fill", "#69b3a2")
        .style("opacity", 0.3)
        .style("stroke", "white")
        .on("mouseover", mouseover )
        .on("mousemove", mousemove )
        .on("mouseleave", mouseleave );

}

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

function socialGraph(dataNodes, dataLinks) {

    // convert to numbers
    dataLinks.forEach(function(d) {
        d.source = +d.source;
        d.target = +d.target;
    });

    var minConnectivity = d3.min(dataNodes, function(d) { return (+d.Followers + +d.Following); });
    var maxConnectivity = d3.max(dataNodes, function(d) { return (+d.Followers + +d.Following); });

    var color = d3.scaleQuantize().range(["rgb(237,248,233)","rgb(186,228,179)","rgb(116,196,118)","rgb(49,163,84)","rgb(0,109,44)"]);
    color.domain([minConnectivity, maxConnectivity]);

    $("social-graph").css("top", $("#navbar").height() + "px");
    $("social-graph").height($(window).height() - $("#navbar").height());

    var margin = {top: 0, right: 0, bottom: 0, left: 0};
    var width = $("#social-graph").width();
    var height = $("#social-graph").height();

    var RADIUS = 15;

    var simulation = d3.forceSimulation(dataNodes)
        .force("link", d3.forceLink(dataLinks).id(d => d.Id))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2));

    var svg = d3.select("#social-graph").append("svg").attr("viewBox", [0, 0, width, height]);
    
    var link = svg.append("g")
        .attr("stroke", "#999")
        .attr("stroke-opacity", 0.6)
        .selectAll("line")
        .data(dataLinks)
        .join("line")
        .attr("stroke-width", 0.8);
    
    var node = svg.append("g")
        .attr("stroke", "#fff")
        .attr("stroke-width", 1.5)
        .selectAll("circle")
        .data(dataNodes)
        .join("circle")
        .attr("r", 10)
        .attr("fill",  function(d) { color(+d.Followers + +d.Following); })
        .call(drag(simulation));

    node.append("title").text(d => d.Username);

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

//execute("select * from MostPopularUsers", mostPopularUsers, 0);
executeCombine("select * from SocialGraph_Nodes", "select * from SocialGraph_Links", socialGraph);

