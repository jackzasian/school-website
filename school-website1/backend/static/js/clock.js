function startClock() {
    const clockElement = document.getElementById('clock');
    function updateClock() {
        clockElement.textContent = new Date().toLocaleTimeString();
    }
    setInterval(updateClock, 1000);
    updateClock();
}

document.addEventListener('DOMContentLoaded', startClock);
