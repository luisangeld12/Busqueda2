
var mymap = L.map('mapid').setView([19.046250, -96.259722], 7);

var apiKey = 'pk.eyJ1IjoibmF5ZWxpcGVyZWEiLCJhIjoiY2thdmZpdDkyMmluMjJxcDF3M2NvdmZ1cSJ9.YuF5Qryse6n1a-a4UcpSSA'

L.tileLayer(`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${apiKey}`, {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
		'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	id: 'mapbox/streets-v11',
	tileSize: 510,
	zoomOffset: -1
}).addTo(mymap);


function creaIcono(ruta, width, height) {
	var icono = L.icon({
		iconUrl: ruta,
		iconSize: [width, height], 
	});
	return icono;
}

var locations = {
	'acayucan': {
		'titulo': 'Acayucan',
		'coordenadas': [17.94919, -94.91459],
		'icon': creaIcono('images/a.png', 50, 38)
	},
	'boca': {
		'titulo': 'Boca del rio',
		'coordenadas': [19.10627, -96.10632],
		'icon': creaIcono('images/boca.png', 30, 30)
	},
	'coatzacoalcos': {
		'titulo': 'Coatzacoalcos',
		'coordenadas': [18.13447, -94.45898],
		'icon': creaIcono('images/coatza.png', 40, 28)
	},
	'aguadulce': {
		'titulo': 'Agua dulce',
		'coordenadas': [18.14259, -94.1436],
		'icon': creaIcono('images/agua.png', 23, 36)
	},
	'huautla': {
		'titulo': 'Huautla de Jiménez',
		'coordenadas': [18.13108, -96.84314],
		'icon': creaIcono('images/huautla.png', 35, 40)
	},
	'fortin': {
		'titulo': 'Fortín de la flores',
		'coordenadas': [18.9017, -96.99896],
		'icon': creaIcono('images/fortin.png', 38, 50)
	},
	'vega': {
		'titulo': 'Vega de Alatorre',
		'coordenadas': [20.03034, -96.65044],
		'icon': creaIcono('images/vega.png', 18, 40)
	},
	'huatusco': {
		'titulo': 'Huatusco',
		'coordenadas': [19.14823, -96.96654],
		'icon': creaIcono('images/huatusco.png', 17, 40)
	},
	'joachin': {
		'titulo': 'Joachín',
		'coordenadas': [18.6407, -96.23095],
		'icon': creaIcono('images/joachin.png', 40, 22)
	},
	'minatitlan': {
		'titulo': 'Minatitlán',
		'coordenadas': [17.99392, -94.5466],
		'icon': creaIcono('images/mina.png', 34, 39)
	},
	'nigromante': {
		'titulo': 'El Nigromante',
		'coordenadas': [17.76323, -95.75574],
		'icon': creaIcono('images/nigromante.png', 40, 38)
	},
	'otatitlan': {
		'titulo': 'Otatitlán',
		'coordenadas': [18.18106, -96.03439],
		'icon': creaIcono('images/otatitlan.png', 33, 39)
	},
	'papantla': {
		'titulo': 'Papantla',
		'coordenadas': [20.45667, -97.31561],
		'icon': creaIcono('images/papantla.png', 67, 60)
	},
	'sanandres': {
		'titulo': 'San Andrés Tuxtla',
		'coordenadas': [18.44412, -95.21302],
		'icon': creaIcono('images/sanandres.png', 40, 34)
	},
	'tecolutla': {
		'titulo': 'Tecolutla',
		'coordenadas': [20.47955, -97.01012],
		'icon': creaIcono('images/tecolutla.png', 40, 31)
	},
	'teziutlan': {
		'titulo': 'Teziutlán',
		'coordenadas': [19.81601, -97.35705],
		'icon': creaIcono('images/te.png', 40, 28)
	},
	'alvarado': {
		'titulo': 'Alvarado',
		'coordenadas': [18.76961, -95.75894],
		'icon': creaIcono('images/alvarado.png', 40, 20)
	},
	'xalapa': {
		'titulo': 'Xalapa',
		'coordenadas': [19.54377, -96.91018],
		'icon': creaIcono('images/xalapaMarker.png', 18, 31)
	},
	'yanga': {
		'titulo': 'Yanga',
		'coordenadas': [18.82928, -96.80027],
		'icon': creaIcono('images/yanga.png', 20, 40)
	},
	'zempoala': {
		'titulo': 'Zempoala',
		'coordenadas': [19.44688, -96.40507],
		'icon': creaIcono('images/zempoala.png', 45, 20)
	},
};

Object.entries(locations).forEach(site => pintaMarker(site));

function pintaMarker(item) {
	//console.log(item);
	if (item[1].icon) {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo, icon: item[1].icon}).addTo(mymap);
	} else {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo}).addTo(mymap);
	}
}

// create a red polyline from an array of LatLng points
var ruta1 = [
	locations.aguadulce.coordenadas,
	locations.coatzacoalcos.coordenadas,
	locations.sanandres.coordenadas,
	locations.alvarado.coordenadas,
	locations.boca.coordenadas,
	locations.zempoala.coordenadas,
	locations.vega.coordenadas,
	locations.tecolutla.coordenadas,
	locations.papantla.coordenadas,
	locations.teziutlan.coordenadas,
	locations.xalapa.coordenadas,
	locations.huatusco.coordenadas,
	locations.fortin.coordenadas,
	locations.yanga.coordenadas,
	locations.joachin.coordenadas,
	locations.otatitlan.coordenadas,
	locations.nigromante.coordenadas,
	locations.acayucan.coordenadas,
	locations.minatitlan.coordenadas,
	locations.coatzacoalcos.coordenadas,
];

var ruta2 = [
	locations.sanandres.coordenadas,
	locations.acayucan.coordenadas,
];

var ruta3 = [
	locations.alvarado.coordenadas,
	locations.otatitlan.coordenadas,
	locations.huautla.coordenadas,
	locations.fortin.coordenadas,
];

var ruta4 = [
	locations.joachin.coordenadas,
	locations.boca.coordenadas,
];

var ruta5 = [
	locations.boca.coordenadas,
	locations.xalapa.coordenadas,
	locations.zempoala.coordenadas,
];

var ruta6 = [
	locations.xalapa.coordenadas,
	locations.vega.coordenadas,
	locations.papantla.coordenadas,
];

var polyline = L.polyline([ruta1, ruta2, ruta3, ruta4, ruta5, ruta6],{color: 'green'}).addTo(mymap);
