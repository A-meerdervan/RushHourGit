
tempertature =[]
date =[]
array2 =[]
array =document.getElementById('data').innerHTML
array = array.split('\n');
for (var i = 0; i < 366; i++){
  array2.push(array[i].split(','));
}

for (var i = 0; i < 366; i++){
  tempertature.push(array2[i][1]);
  date.push(array2[i][0]);
}
// maak de canvas aan
var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
width = 1000
height = 500
ctx.canvas.width = width
ctx.canvas.height = height



transformx = createTransform([0,450],[0,width])
transformy = createTransform([-200,400],[height,0])

distanceFromLeft = transformx(30)
console.log('hello')
// y = 0
ctx.strokeRect(distanceFromLeft,transformy(0),transformx(366),1)
//x-as
ctx.strokeRect(distanceFromLeft,transformy(-100),transformx(366),1)
// y-as
ctx.beginPath();
ctx.moveTo(distanceFromLeft,transformy(350));
ctx.lineWidth = 2;
ctx.lineTo(distanceFromLeft,transformy(-100));
ctx.stroke()
// zet alle maanden er in met een streepje
months = ["January","February","March","April","May","June","July","August",
"September","October","November","December"]

for ( var l = 0; l < 12; l++){
  ctx.font = "13px serif";
  ctx.fillText(months[l], transformx(30.5*l+30),transformy(-150));
  ctx.beginPath();
  // weet niet waar de extra lijn vandaan komt maar vind het niet netjes om alles
  //zonder loop te doen??
  ctx.moveTo(transformx(30+30.5*(l+1)),transformy(-100));
  ctx.lineTo(transformx(30+30.5*(l+1)),transformy(-90));
  ctx.stroke();
};
ctx.font = '800 20px Arial'
ctx.fillText("month",transformx(391),transformy(-120))


ctx.font = "13px serif"
// zet de temperatuur en het streepje erbij
ctx.fillText(" 0",transformx(20),transformy(0))
ctx.strokeRect(distanceFromLeft-10,transformy(0),10,1)
ctx.fillText("10",transformx(20),transformy(100))
ctx.strokeRect(distanceFromLeft-10,transformy(100),10,1)
ctx.fillText("20",transformx(20),transformy(200))
ctx.strokeRect(distanceFromLeft-10,transformy(200),10,1)
ctx.fillText("30",transformx(20),transformy(300))
ctx.strokeRect(distanceFromLeft-10,transformy(300),10,1)
ctx.fillText("-10",transformx(20),transformy(-100))
ctx.strokeRect(distanceFromLeft-5,transformy(-100),5,1)

// voor elke variabele in de array line aanmaken!
k = 30
for ( var i = 0 ; i < 366; i++){
  ctx.lineTo(transformx(k),transformy(tempertature[i]))
  k++
};
ctx.stroke()
ctx.font = "48px serif";
ctx.fillText("Maximum Temperature in the Bild(NL) 1996", 90, 50);



function createTransform(domain, range){
	// domain is a two-element array of the domain's bounds
	// range is a two-element array of the range's bounds
	// implement the actual calculation here b = range[0] - a*domain[0]
	// a = range[1]-range[0]/domain[1]-domain[0]
	var alpha = (range[1]-range[0])/(domain[1]-domain[0]) ;
	var beta = range[0]-alpha*domain[0];

	// get rid of the padding of the range
	return function(x){

	return (alpha * x) + beta;
	};
}

// to use this for instance:
var transform = createTransform([10, 20], [10, 20]);
//console.log(transform(15)); //should return 15!!
ctx.font = "30px serif"
ctx.rotate((Math.PI/180*-90))
ctx.fillText('Temperature in Celcius',transformx(-170),transformy(355))
