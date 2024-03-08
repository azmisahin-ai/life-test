// 3D
var scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000); // İsterseniz bir arka plan rengi belirleyebilirsiniz.
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

camera.position.z = 9;

var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);
// Sahnenin arka plan rengini şeffaf yap
renderer.setClearAlpha(0);


function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

window.addEventListener('resize', onWindowResize, false);

// Dışarıda bir bayrak tanımla
let animateRunning = false;

function animate() {
  requestAnimationFrame(animate);

  // Diğer animasyon kodları...

  // Sahneyi render etme
  renderer.render(scene, camera);
}

// Animasyon döngüsü dışında bayrağı sıfırla
animateRunning = false;

function clearScene() {
  // Sahnedeki her objeyi kaldır
  scene.traverse(function (object) {
    if (object instanceof THREE.Mesh) {
      // Mesh objesini dispose et
      object.geometry.dispose();
      object.material.dispose();
    }
  });

  // Sahnedeki tüm ışıkları kaldır
  scene.traverse(function (object) {
    if (object instanceof THREE.Light) {
      object.dispose();
    }
  });

  // Sahne ile ilgili diğer unsurları dispose et
  scene.dispose();

  // Yeni bir sahne oluştur
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x000000); // İsterseniz bir arka plan rengi belirleyebilirsiniz.
}


// Socket
var socket = io.connect(
  "http://" + document.domain + ":" + location.port
);

socket.on("connect", function () {
  console.log("Connected to server");
});

universe = {
  generation: 0,
  organisms: []
}





socket.on("life", function (data) {
  const status = JSON.parse(data);
  document.getElementById("life_status").innerText = status
  document.getElementById("life_status").className = "text-" + status
})


// Sahnedeki bir objeyi ismine göre kaldıran fonksiyon
function removeObjectByName(name) {
  try {
    scene.traverse(function (object) {
      if (object.name === name) {
        scene.remove(object);
      }
    });
  } catch (error) {

  }

}

function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

socket.on("reproduce", function (data) {
  const organism = JSON.parse(data);
  console.log("organism", organism);
  document.getElementById("organism_status").innerText = organism.name + " reproduce";




  // Yeni yuvarlak objeyi oluştur
  // Yeni yuvarlak objeyi oluştur
  const radius = 0.2;
  const widthSegments = 5;
  const heightSegments = 5;
  const geometry = new THREE.SphereGeometry(radius, widthSegments, heightSegments);

  // Rastgele bir renk oluştur
  const material = new THREE.MeshBasicMaterial({ color: getRandomColor() });

  // eklioruz
  const obj = new THREE.Mesh(geometry, material);

  // Ayrı ayrı koordinatları ayarla
  obj.name = organism.name
  obj.position.x = organism.position.x;
  obj.position.y = organism.position.y;
  obj.position.z = organism.position.z;

  // Sahneye ekle
  scene.add(obj);

  // Tek bir animasyon döngüsü başlat
  if (!animateRunning) {
    animateRunning = true; // Animasyonun zaten çalışıp çalışmadığını kontrol etmek için bir bayrak
    animate();
  }
})

socket.on("died", function (data) {
  organism = JSON.parse(data);
  console.log("died", organism)
  document.getElementById("organism_status").innerText = organism.name + " died"

  removeObjectByName(organism.name)
})

// all data
socket.on("update-ui", function (data) {
  universe = JSON.parse(data);
  console.log("universe", universe)
  document.getElementById("reproduction_status").innerText = universe.organisms.length
  document.getElementById("generation_status").innerText = universe.generation
  // // Transformation
  // for (var name in datasource) {
  //   if (!organisms[name]) {
  //     var geometry = new THREE.BoxGeometry();
  //     var material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
  //     organisms[name] = new THREE.Mesh(geometry, material);
  //     scene.add(organisms[name]);
  //   }

  //   organisms[name].position.x = positions[name].x;
  //   organisms[name].position.y = positions[name].y;
  //   organisms[name].position.z = positions[name].z;
  // }
});


function updateFormData() {
  // Formdaki verileri al
  const reproductionValue = document.getElementById('reproduction').value;
  const generationValue = document.getElementById('generation').value;

  clearScene()
  // Verileri sokete gönder
  socket.emit('update-universe', { reproduction: reproductionValue, generation: generationValue });
}
