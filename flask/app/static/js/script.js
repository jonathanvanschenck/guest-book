// This holds all the jquery and socket.io javascript for the client connections

// useful variables
var log = $("#log")
var name_input = $("#name-input")
var message_input = $("#message-input")

// Attach Socket.io
var socket = io();

socket.on("connect", function() {
  // console.log('connected');

  // Activate Post Button
  $("#post-button")
    .toggleClass("btn-warning",false)
    .toggleClass("btn-primary",true)
    [0].setCustomValidity("");
});

socket.on("disconnect", function () {
  socket.emit("disconnect_request");
  // console.log('disconnected');

  // Deactivate Post Button
  $("#post-button")
    .toggleClass("btn-warning",true)
    .toggleClass("btn-primary",false)
    [0].setCustomValidity("No server connection");
});

socket.on("log_in_console", function(msg) {
  // log whatever message into the console (debugging)
  console.log(msg);
});

socket.on("render_post", function(msg) {
  // render a single post into the log div
  render_post(msg);
});

socket.on("render_post_list", function(msg) {
  // render a list of posts into the log div
  log.empty();
  for (let post of msg.post_list) {
    render_post(post);
  }
});

attemptPost = function() {
  // Send post to server for broadcast
  socket.emit(
    "broadcast_post",
    {
      name: name_input[0].value,
      message: message_input[0].value
    }
  )
  // Reset form
  name_input[0].value = "";
  message_input[0].value = "";

};

render_post = function(msg) {
  // Get approximate post time of a post
  let post_time = new Date(Date.now()-1000*msg.timedelta);
  // Create the new post html, hidden
  let new_post = $("<div>")
    .toggleClass("post-container")
    .toggleClass("card")
    .toggleClass("mb-1") // set margin
    .toggleClass("bg-light").append(
      $("<h5>")
      .toggleClass("card-title")
      .toggleClass("p-1")
      .toggleClass("mb-0")
      .text(msg.name + " : ").append(
          $("<time>")
          .toggleClass("timeago")
          .toggleClass('text-muted')
          .attr("datetime",post_time.toISOString())
          .text($.timeago(post_time.toISOString()))
        )
    ).append(
      $("<p>")
      .toggleClass('card-body')
      .toggleClass('p-2')
      .toggleClass("mb-1")
      .text(msg.message)
    ).hide()
  // Attach the post to the log div
  log.prepend(new_post)
  // Animate entrance
  new_post.slideDown(msg.skip_animate ? 0 : 1000)
}


// Update all the time stamps
window.setInterval(function() {
  $("time.timeago").timeago();
}, 1000*60);
