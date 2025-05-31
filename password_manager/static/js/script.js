function setCurrentTheme() {
    const currentTheme = localStorage.getItem('theme')
    if (currentTheme === 'dark') {
        localStorage.setItem('theme', 'dark')
    } else if (currentTheme === 'light') {
        localStorage.setItem('theme', 'light')
    } else {
        localStorage.setItem('theme', 'light')
    }
}

function setTheme() {
    const currentTheme = localStorage.getItem('theme')
    const body = document.body;
    if (currentTheme === 'dark') {
        body.classList.add("dark-mode");
        body.classList.remove("light-mode");
    } else if (currentTheme === 'light') {
        body.classList.add("light-mode");
        body.classList.remove("dark-mode");
    }
}

function toggleTheme() {
    const currentTheme = localStorage.getItem('theme')
    const body = document.body;
    if (currentTheme === 'dark') {
        localStorage.setItem('theme', 'light')
        body.classList.add("light-mode");
        body.classList.remove("dark-mode");
    } else if (currentTheme === 'light') {
        localStorage.setItem('theme', 'dark')
        body.classList.add("dark-mode");
        body.classList.remove("light-mode");
    }
}

document.getElementById("toggle-theme").addEventListener("click", function () {
    toggleTheme()
});

window.addEventListener("load", function () {
    setCurrentTheme()
    setTheme()
});