function jump_to(country){
    console.log(window.location.href)
    const part_url=window.location.href.substring(0,window.location.href.indexOf("country"))
    window.location.href = part_url + "country/" + country.toLowerCase() +"/"
}