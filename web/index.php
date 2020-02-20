
<?php

exec("/home/pi/fallblatt/python/saysomething.sh 'hallo'");


?>


<!DOCTYPE html>
<html>
	<head>
		<title>Fallblatt</title>
		<style>
			@font-face {
				font-family: "SBB";
				src: url("./font/SBBWeb-Condensed-Bold.woff") format("woff2"),
					url("./font/SBBWeb-Condensed-Bold.woff2") format("woff");
			}
			body{
				font-family: sans-serif;
			}
			#inputForm{
				margin: 20px;
				text-align: center;
			}
			.segment{
				background-color: #26356e;
				border: 1px #151e3d solid;
				color: #FFFFFF;
				height: calc(6.666vw * 1.2);
				font-size: calc(6.666vw * 1.0);
				text-align: center;
				overflow: hidden;
			}
			#preview{
				display: grid;
				grid-gap: 0.5vw;
				grid-template-columns: repeat(15, 1fr);
				font-family: SBB;
			}
		</style>
	</head>
	<body>
		<form id="inputForm" method="post" action="">
			<input type="text" id="input" name="text" size="30" maxlength="30">
			<input type="submit" value="Send">
		</form>
		<div id="preview"></div>
	</body>
	<script>
		const lineLength = 15;
		const lineCount = 2;
		const segmentCount = lineLength*lineCount;
		
		const input = document.getElementById("input");
		const preview = document.getElementById("preview");
		
		const segments = [];
		for(let segment = 0; segment < segmentCount; segment++){
			let segment = document.createElement("div");
			segment.className = "segment";
			segments.push(segment);
			preview.appendChild(segment);
		}
		
		
		input.addEventListener("input", function(){
			let text = input.value;
			text = text.replace(/[^a-zA-Z0-9\-\.\/ ]/g, " ");
			text = text.substring(0, lineLength*lineCount);
			text = text.toUpperCase();
			for(let i in segments){
				console.log(i);
				segments[i].innerHTML = text.substr(i, 1);
			}
		});
	</script>
</html>