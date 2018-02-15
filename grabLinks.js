linksArray = (() => { 
  var jobDivs = document.getElementsByClassName("_Rm");
  // convert HTMLCollection to array 
  var jobDivsArray = [].slice.call(jobDivs)
  var jobLinks = []; 
  jobDivsArray.forEach((job) => { 
    jobLinks.push(job.innerText);
    console.log(job.innerText);
  }) 
  return jobLinks
})()                 

/*
copyLinks = () => { 
  if (document.selection) { 
  var copyText = [].slice.call(document.getElementsByClassName("_Rm"));
  var textRange = document.body.createTextRange();
  copyText.forEach((elem) => { 
     textRange.moveToElementText(elem);
  });
  textRange.select().createTextRange();
  document.execCommand("copy"); 
  } else if (window.getSelection) { 
    var copyElements = [].slice.call(document.getElementsByClassName("_Rm")) 
    var textRange = document.createRange();
    copyElements.forEach((elem) => { 
      textRange.selectNode(elem);
      window.getSelection().addRange(textRange);
    });
    document.execCommand("copy");
    console.log(textRange);
    console.log("Copied ", copyElements.length, "items");
  }
}
*/
