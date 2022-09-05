

document.getElementById("refresh").onclick = () => {
    const xhr = new XMLHttpRequest();
	xhr.open("GET", '/get_data/')
	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json")
	xhr.setRequestHeader("Access-Control-Allow-Origin", window.location.host)
	xhr.send()
	xhr.onload = () => {
        let data = JSON.parse(xhr.responseText)
        console.log(data)
    }
}