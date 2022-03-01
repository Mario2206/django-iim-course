const messageList = document.querySelector(".message-list");
const messageInput = document.querySelector(".message-form--input")
const messageForm = document.querySelector(".message-form")


const socket = new WebSocket(
	"ws://" + window.location.host + "/ws/messenger"
);

socket.onmessage = (e) => {
    const data = JSON.parse(e.data)
    messageList.innerHTML += `
    <div class='message'>
        <p>${data.message}</p>
    </div>
    `
}

socket.onclose = () => {
    console.error("Socket closed !");
}

messageInput.focus();

messageForm.addEventListener("submit", (e)=> {
    e.preventDefault()
    const message = messageInput.value

    if(!message) return  alert("Your message is empty")

    socket.send(JSON.stringify({ message }));

    messageInput.value = ""


})