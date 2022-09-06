

document.getElementById("refresh").onclick = () => {
	document.getElementsByTagName('body')[0].classList.add("loader-visible");
    const xhr = new XMLHttpRequest();
	xhr.open("GET", '/get_data/')
	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json")
	xhr.setRequestHeader("Access-Control-Allow-Origin", window.location.host)
	xhr.send()
	xhr.onload = () => {
        let data = JSON.parse(xhr.responseText)
		document.getElementsByClassName("content")[0].innerHTML = data["content"]
		document.getElementsByTagName('body')[0].classList.remove("loader-visible");

    }
}

document.getElementById("selector-filter").onchange = () => {

	let xhr = new XMLHttpRequest();
	xhr.open("GET", '/filter_data/?order=' + document.getElementById("selector-filter").value)
	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json")
	xhr.setRequestHeader("Access-Control-Allow-Origin", window.location.host)
	xhr.send()
	xhr.onload = () => {
        let data = JSON.parse(xhr.responseText)
		document.getElementsByClassName("content")[0].innerHTML = data["content"]
    }
}