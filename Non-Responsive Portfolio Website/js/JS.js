	function goBack(){
		window.history.back()
	}
	function validateForm(){
		var names = document.forms["contactform"]["Name"].value;
		var mails = document.forms["contactform"]["mail"].value;
		var messages = document.forms["contactform"]["message"].value;
				
		if (names == "" || mails == "" || messages == ""){
			alert("Empty fields found. Please fill");
		}	
		else{
			alert("Thank you for the feedback");
		}
	}
	
	window.onscroll = function()
	{scrollFunction()};
	
	function scrollFunction(){
		if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50){
			document.getElementById("topbtn").style.display = "block";
			document.getElementById("logo").style.fontSize = "16px";
		}
		else{
			document.getElementById("topbtn").style.display = "none";
			document.getElementById("logo").style.fontSize = "25px";
		}
	}
	function topFunction(){
		document.body.scrollTop= 0;
		document.documentElement.scrollTop = 0;
	}
	
	var i=0;
	var images = [];
	var time = 1500;
	images[0]='./images/blog1.jpg';
	images[1]='./images/blog1.1.jpg';
	images[2]='./images/blog1.2.jpg';
	images[3]='./images/blog1.3.jpg';
	
	function slideshow(){
		document.slide.src = images[i];
		if(i < images.length - 1){
			i++;
		}
		else{
			i=0;
		}
		setTimeout("slideshow()",time);
	}
	window.onload = slideshow;