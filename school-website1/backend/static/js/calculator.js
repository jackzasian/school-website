function initCalculator() {
    const calculator = document.getElementById('calculator');
    calculator.innerHTML = `
        <input type="text" id="calc-display" disabled />
        <div>
            <button onclick="inputCalc('1')">1</button>
            <button onclick="inputCalc('2')">2</button>
            <button onclick="inputCalc('3')">3</button>
            <button onclick="inputCalc('+')">+</button>
        </div>
        <div>
            <button onclick="inputCalc('4')">4</button>
            <button onclick="inputCalc('5')">5</button>
            <button onclick="inputCalc('6')">6</button>
            <button onclick="inputCalc('-')">-</button>
        </div>
        <div>
            <button onclick="inputCalc('7')">7</button>
            <button onclick="inputCalc('8')">8</button>
            <button onclick="inputCalc('9')">9</button>
            <button onclick="inputCalc('*')">*</button>
        </div>
        <div>
            <button onclick="inputCalc('0')">0</button>
            <button onclick="calculate()">=</button>
            <button onclick="clearCalc()">C</button>
            <button onclick="inputCalc('/')">/</button>
        </div>
    `;
}

function inputCalc(val) {
    const display = document.getElementById('calc-display');
    display.value += val;
}

function calculate() {
    const display = document.getElementById('calc-display');
    try {
        display.value = eval(display.value);
    } catch {
        display.value = 'Error';
    }
}

function clearCalc() {
    document.getElementById('calc-display').value = '';
}

document.addEventListener('DOMContentLoaded', initCalculator);
