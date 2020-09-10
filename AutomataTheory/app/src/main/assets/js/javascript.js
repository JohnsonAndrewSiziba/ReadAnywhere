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
    let title = document.getElementsByTagName("title")[0].innerHTML
    let url=location.href;
    let urlFilename = url.substring(url.lastIndexOf('/')+1);
    console.log(`Title: ${title}, File: ${urlFilename}`);
    JSReceiver.getPageDetails(title, url);
}

function addBookmark(){

}

function toggleContents(){

}


////================================FUNCTION CALLS==========================///////////

initialize();
