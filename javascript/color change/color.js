var isTrue = confirm("do you want to change color of body...")

if(isTrue){
    document.body.style.backgroundColor = "red"
    document.body.style.color = "#ffff"
    document.body.style.display = "flex"
    document.body.style.alignItems = "center"
    document.body.style.justifyContent = "center"
    document.body.style.minHeight = "100vh"
}

else{
    console.log("ok.!")
}
