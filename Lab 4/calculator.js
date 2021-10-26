function reset() {
    document.getElementById("screen").value = "";
}

function inputs(value) {
    document.getElementById("screen").value += value;
    let expression = document.getElementById("screen").value
    if (expression.includes("+")) {
        let operator = '+' + expression.split('+').pop();
        return operator
    }
    if (expression.includes("-")) {
        let operator = '-' + expression.split('-').pop();
        return operator
    }
    if (expression.includes("/")) {
        let operator = '/' + expression.split('/').pop();
        return operator
    }
    if (expression.includes("*")) {
        let operator = '*' + expression.split('*').pop();
        return operator
    } 
}

function calculate() {
    if ((document.getElementById("screen").value.includes("+") == true) || document.getElementById("screen").value.includes("-") == true || document.getElementById("screen").value.includes("/") == true || document.getElementById("screen").value.includes("*") == true)  {
        let displayexpression = document.getElementById("screen").value;
        let answer = eval(displayexpression);
        document.getElementById("screen").value = answer;
        console.log(typeof document.getElementById("screen").value);
        console.log(document.getElementById("screen").value);

    }
    else {
        document.getElementById("screen").value += operator;
        let displayexpression = document.getElementById("screen").value;
        let answer = eval(displayexpression)
        document.getElementById("screen").value = answer;

    }
}