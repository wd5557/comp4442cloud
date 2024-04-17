function navbar() {
    let a = document.querySelector("#navbarToggle");
    let b = document.querySelectorAll(".des");
    let isResized = false;

    function toggleVisibility() {
        for (let i = 0; i < b.length; i++) {
            if (b[i].style.display === "none" || b[i].style.display === "") {
                b[i].style.display = "block";
            } else {
                b[i].style.display = "none";
            }
        }
    }

    function handleResize() {
        if (window.innerWidth >= 1151) {
            for (let i = 0; i < b.length; i++) {
                b[i].style.display = "block";
            }
            isResized = false;
        } else {
            if (!isResized) {
                for (let i = 0; i < b.length; i++) {
                    b[i].style.display = "none";
                }
                isResized = true;
            }
        }
    }

    a.addEventListener("click", toggleVisibility);
    window.addEventListener("resize", handleResize);
}

navbar();