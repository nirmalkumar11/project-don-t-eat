// const textarea = document.getElementById("input");
// const messages = document.getElementById("chatContainer");

// textarea.addEventListener("input", () => {
//     textarea.style.height = "auto";
//     textarea.style.height = textarea.scrollHeight + "px";

//     // Keep messages visible
//     messages.scrollTop = messages.scrollHeight;
// });

// image input

const fileInput = document.getElementById("fileInput");
const attachBtn = document.getElementById("attachBtn");
const previewContainer = document.getElementById("previewContainer");

attachBtn.addEventListener("click", () => fileInput.click());

fileInput.addEventListener("change", () => {
    Array.from(fileInput.files).forEach(file => {
        if (!file.type.startsWith("image/")) return;

        const wrapper = document.createElement("div");
        wrapper.className = "preview-wrapper";

        const img = document.createElement("img");
        img.src = URL.createObjectURL(file);
        img.className = "preview-img";

        const removeBtn = document.createElement("span");
        removeBtn.className = "remove-btn";
        removeBtn.innerHTML = "&times;";

        removeBtn.onclick = () => {
            URL.revokeObjectURL(img.src); // memory cleanup
            wrapper.remove();
        };

        wrapper.append(img, removeBtn);
        previewContainer.appendChild(wrapper);
    });

    fileInput.value = ""; // allow re-upload same image
});



// const fileInput = document.getElementById("fileInput");
// const attachBtn = document.getElementById("attachBtn");
// const previewContainer = document.getElementById("previewContainer");

// attachBtn.addEventListener("click", () => fileInput.click());

// fileInput.addEventListener("change", () => {
//     Array.from(fileInput.files).forEach(file => {
//         if (!file.type.startsWith("image/")) return;

//         const wrapper = document.createElement("div");
//         wrapper.className = "preview-wrapper";

//         const img = document.createElement("img");
//         img.src = URL.createObjectURL(file);
//         img.className = "preview-img";

//         const removeBtn = document.createElement("span");
//         removeBtn.className = "remove-btn";
//         removeBtn.innerHTML = "&times;";

//         removeBtn.onclick = () => {
//             URL.revokeObjectURL(img.src); // memory cleanup
//             wrapper.remove();
//         };

//         wrapper.append(img, removeBtn);
//         previewContainer.appendChild(wrapper);
//     });

//     fileInput.value = ""; // allow re-upload same image
// });

// let chatContainer = document.getElementById('chatContainer ');

// let userChat = document.createElement("div");
// let input = document.createElement("p")
// userChat.classList.add("User-chat-style")
//     //agent-response-style
// input.textContent = "hello, how are you"
// userChat.appendChild("input")
// chatContainer.appendChild("userChat")