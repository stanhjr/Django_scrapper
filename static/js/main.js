

document.getElementById("refresh").onclick = () => {
	document.getElementsByTagName('body')[0].classList.add("loader-visible");
    let xhr = new XMLHttpRequest();
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


function setDeleteBtn(){
	let btnDeleteList = document.getElementsByClassName("btn-delete")
	for (let i = 0; i < btnDeleteList.length; i++ ){
		let btnDelete = document.getElementsByClassName("btn-delete")[i]
		document.getElementsByClassName("btn-delete")[i].onclick = () => {
			DeleteItem(document.getElementsByClassName("btn-delete")[i])
		}
	}

}


function DeleteItem(btnElem){
	let xhr = new XMLHttpRequest();
	let csrftoken = getCookie('csrftoken')
	console.log(csrftoken)
	xhr.open("DELETE", '/delete_item/' + btnElem.value + '/')
	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json")
	xhr.setRequestHeader("X-CSRFToken", csrftoken)
	xhr.setRequestHeader("Access-Control-Allow-Origin", window.location.host)
	xhr.send()
	xhr.onload = () => {
		console.log(xhr.status)
		if (xhr.status === 204){
			btnElem.parentElement.parentElement.parentElement.remove()
		}


    }

}


function getCookie(cname) {
     let name = cname + "=";
     let ca = document.cookie.split(';');
     for(let i=0; i<ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if(c.indexOf(name) == 0)
           return c.substring(name.length,c.length);
     }
     return ""
}