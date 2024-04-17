var isTrue = confirm("do you want to change your color")

if (isTrue){
    var a = prompt("enter your color name")
    document.body.style.backgroundColor = a
}

else{
    console.log("ok...")
}