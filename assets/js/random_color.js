function changeColor() {
    var colors = [
        "#C6DDF0", "#F06449", "#5BC3EB", "#540D6E", "#EE4266", "#0EAD69",
        "#E0FF4F", "#FF2ECC", "#00272B", "#00A6FB", "#F02D3A", "#D9BBF9"
    ];
    var color = colors[Math.floor(Math.random() * colors.length)];
    document.querySelector("#homepage_hero_party").style.color = color;
}

setInterval(changeColor, 1000);