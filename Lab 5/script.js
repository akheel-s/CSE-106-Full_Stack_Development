var url = "https://amhep.pythonanywhere.com/grades";

function loadAll(){
    let xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.onreadystatechange = function () {
        var persons = JSON.parse(xhr.responseText);
        var string = JSON.stringify(persons)
        document.getElementById("allstudents").innerHTML = string;
        };
        xhr.send();
}

function search(){
    var input = document.getElementById("searchname").value;
    let xhr = new XMLHttpRequest();
    console.log(url + "/" + input)
    xhr.open("GET", url + "/" + input);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            var persons = JSON.parse(xhr.responseText);
            var string = JSON.stringify(persons)
            document.getElementById("personinfo").innerHTML = string;
    }};
        xhr.send();
}


function adding(){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    document.getElementById("added").innerHTML = "Student and grade added.";
    var input1 = document.getElementById("addname").value;
    var input2 = document.getElementById("addgrade").value;
    var output = '{"name": "' + input1 + '", "grade": ' + input2 + '}';
    xhr.send(output);
}

function editing(){
    var input = document.getElementById("editname").value;
    var xhr = new XMLHttpRequest();
    xhr.open("PUT", url + "/" + input);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    var input2 = document.getElementById("editgrade").value;
    var output = '{"grade": ' + input2 + '}';
    xhr.send(output);
    document.getElementById("edited").innerHTML = "Grade edited.";
}

function deletestudent(){
    var input2 = document.getElementById("deletename").value;
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", url + "/" + input2);
    xhr.setRequestHeader("Accept", "application/json");
    document.getElementById("deleted").innerHTML = "Student successfully deleted.";
    xhr.send();
}