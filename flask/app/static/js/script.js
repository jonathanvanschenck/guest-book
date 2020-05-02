// This holds all the jquery and socket.io javascript for the client connections

// useful variables
var log = $("#log")
var name_input = $("#name-input")
var message_input = $("#message-input")

// Attach Socket.io
var socket = io();

socket.on("connect", function() {
  console.log('connected');
});
socket.on("disconnect", function () {
  socket.emit("disconnect_request");
  console.log('disconnected');
});
socket.on("log_in_console", function(msg) {
  // log whatever message into the console (debugging)
  console.log(msg);
});
socket.on("render_post", function(msg) {
  // render a single post into the log div
  render_post(msg);
});

attemptPost = function() {
  socket.emit(
    "broadcast_post",
    {
      name: name_input[0].value,
      message: message_input[0].value,
      skip_animate: false
    }
  )
};

render_post = function(msg) {
  // Create the new post html, hidden
  let new_post = $("<div>")
    .toggleClass("post-container").append(
      $("<h4>").text(msg.name)
    ).append(
      $("<p>").text(msg.message)
    ).hide()
  // Attach the post to the log div
  log.prepend(new_post)
  // Animate entrance
  new_post.slideDown(msg.skip_animate ? 0 : 1000)
}
