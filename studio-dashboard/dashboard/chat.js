const chatBox = document.getElementById("chatBox");

const evtSource = new EventSource("http://127.0.0.1:3333/chat/stream");

evtSource.onmessage = function(event) {
  const div = document.createElement("div");
  div.className = "text-zinc-400 text-sm";
  div.innerText = event.data;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
};
