// This holds all the jquery and socket.io javascript for the client connections

// useful variables
var log = $("#log")
var name_input = $("#name-input")
var message_input = $("#message-input")

attemptPost = function() {
  render_post({
    name: name_input[0].value,
    message: message_input[0].value,
    skip_animate: false
  })
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
  new_post.slideDown(msg.skip_animate ? 0 : 600)
}
