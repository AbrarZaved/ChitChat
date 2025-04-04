console.log("Hello");
document.addEventListener("DOMContentLoaded", function () {
  var chatRoomName = JSON.parse(
    document.getElementById("json-chatroomname").textContent
  );
  const username = JSON.parse(
    document.getElementById("json-username").textContent
  );

  console.log(chatRoomName);

  // Connect to WebSocket
  const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/" + chatRoomName + "/"
  );

  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.message) {
      console.log("Message: " + data.message);
      let html = `
                    <div class="message shadow-lg p-3 rounded-lg bg-blue-300 m-3">
                        <div class="text-sm text-gray-500">${data.username}</div>
                        <div class="text-lg mt-2">${data.message}</div>
                        <div class="text-sm text-gray-500 mt-2">Now</div>
                    </div>
                `;
      document.querySelector("#chat-messages").innerHTML += html;
      document.querySelector("#chat-messages").scrollTop =
        document.querySelector("#chat-messages").scrollHeight; // Auto scroll to bottom
    } else {
      alert("Message was empty");
    }
  };

  chatSocket.onclose = function (e) {
    console.log("Chat socket closed");
  };

  document.getElementById("send-button").onclick = function (e) {
    e.preventDefault();
    var message = document.getElementById("message").value;
    if (message.trim() === "") {
      return;
    }
    console.log("Sending Message: " + message);
    chatSocket.send(
      JSON.stringify({
        message: message,
        username: username,
        room: chatRoomName,
      })
    );
    document.getElementById("message").value = ""; // Clear input after sending
  };
});
