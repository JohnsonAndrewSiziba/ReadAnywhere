'use strict';

function test() {
//   document.write("Ramona Flowers");
}

function loginDomain() {
    document.getElementById('gadget_url').value = 'agri';
}

function initialize(){
    getPageDetails();
}

function getPageDetails(){
    //let title = document.getElementsByTagName("title")[0].innerHTML
    let title = $(".tutorial-content h1").text()
    let intro = $(".tutorial-content p:first").text()
    let url=location.href;
    let urlFilename = url.substring(url.lastIndexOf('/')+1);
    console.log(`Title: ${title}, Intro: ${intro}, File: ${urlFilename}`);
    JSReceiver.getPageDetails(title, url, intro);
}

function addBookmark(){

}

function toggleContents(){

}

function contents(){
    $('#myModal').modal('toggle');
}


////================================FUNCTION CALLS==========================///////////



$(document).ready(function() {
      initialize();
});
