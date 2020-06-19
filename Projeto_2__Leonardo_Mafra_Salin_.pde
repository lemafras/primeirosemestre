// importando bibliotecas de áudio e vídeo
import ddf.minim.*;
import processing.video.*;

// criação de instâncias para as bibliotecas
Minim som;
AudioPlayer musica1, musica2, musica3, musica4, musica5, musica6;
Movie video1, video2, video3, video4, video5, video6;

// criação de objeto do tipo Processing Image
PImage img1, img2, img3, img4, img5, img6, img0;

// variável para controle de fluxo
int var = 0;

// função chamada no início da aplicação, somente uma vez
void setup() {
  background(0,0,0); // fundo preto
  size(940, 480); // tamanho da tela
  img0 = loadImage("capasp.jpg");
  img1 = loadImage("capa1.png");
  img2 = loadImage("capa2.jpg");
  img3 = loadImage("capa3.jpg");
  img4 = loadImage("capa4.jpg");
  img5 = loadImage("capa5.png");
  img6 = loadImage("capa6.png");
  som = new Minim(this);
  musica1 = som.loadFile("musica1.mp3");
  musica2 = som.loadFile("musica2.mp3");
  musica3 = som.loadFile("musica3.mp3");
  musica4 = som.loadFile("musica4.mp3");
  musica5 = som.loadFile("musica5.mp3");
  musica6 = som.loadFile("musica6.mp3");
  video1 = new Movie(this,"video01.m4v");
  video2 = new Movie(this,"video02.m4v");
  video3 = new Movie(this,"video03.m4v");
  video4 = new Movie(this,"video04.m4v");
  video5 = new Movie(this,"video05.m4v");
  video6 = new Movie(this,"video06.m4v");
  
}

// função chamada n vezes por segundo (em loop)
void draw(){
  //menu
  image(img0,300,0);
  //capa
  image(img1,0,0);
  image(img2,0,150);
  image(img3,150,0);
  image(img4,150,150);
  image(img5,0,300);
  image(img6,150,300);
  //videoclipe
  image(video1,300,0);
  image(video2,300,0);
  image(video3,300,0);
  image(video4,300,0);
  image(video5,300,0);
  image(video6,300,0);
  //botão
  fill(79, 47, 79); rect(0,450,300,30); fill(255); text("PAUSE", 125,470);
  fill(79, 47, 79); text("smooth player", 855, 15);
  
  // teste de qual é a imagem
  if (var == 1){
    image(video1,300,0);
    musica1.play();
    musica2.pause();
    musica3.pause();
    musica4.pause();
    musica5.pause();
    musica6.pause();
    video1.play();
    video2.pause();
    video3.pause();
    video4.pause();
    video5.pause();
    video6.pause();
  }
  if (var == 2){
    image(video2,300,0);
    musica2.play();
    musica1.pause();
    musica3.pause();
    musica4.pause();
    musica5.pause();
    musica6.pause();
    video2.play();
    video1.pause();
    video3.pause();
    video4.pause();
    video5.pause();
    video6.pause();
  }
  if (var == 3){
    image(video3,300,0);
    musica3.play();
    musica1.pause();
    musica2.pause();
    musica4.pause();
    musica5.pause();
    musica6.pause();
    video3.play();
    video1.pause();
    video2.pause();
    video4.pause();
    video5.pause();
    video6.pause();
  }
  if (var == 4){
    image(video4,300,0);
    musica4.play();
    musica1.pause();
    musica2.pause();
    musica3.pause();
    musica5.pause();
    musica6.pause();
    video4.play();
    video1.pause();
    video2.pause();
    video3.pause();
    video5.pause();
    video6.pause();
  }
  if (var == 5){
    image(video5,300,0);
    musica5.play();
    musica1.pause();
    musica2.pause();
    musica3.pause();
    musica4.pause();
    musica6.pause();
    video5.play();
    video1.pause();
    video2.pause();
    video3.pause();
    video4.pause();
    video6.pause();
  }
  if (var == 6){
    image(video6,300,0);
    musica6.play();
    musica1.pause();
    musica2.pause();
    musica3.pause();
    musica4.pause();
    musica5.pause();
    video6.play();
    video1.pause();
    video2.pause();
    video3.pause();
    video4.pause();
    video5.pause();
  
  }
  if (var == 7){
    image(img0, 300,0);
    musica1.pause();
    musica2.pause();
    musica3.pause();
    musica4.pause();
    musica5.pause();
    musica6.pause();
    video1.pause();
    video2.pause();
    video3.pause();
    video4.pause();
    video5.pause();
    video6.pause();
    
}
     
  println(mouseX+""+mouseY+""+var);
  
}

// caso o botão seja pressionado, função de acordo é chamada (de dentro da função draw())
void mousePressed(){
  // verificação de coordenadas do mouse em relação as coordenadas de cada botão
 if((mouseX<150) && (mouseY<150)) var=1;
 if((mouseX<150) && (mouseY>150) && (mouseY<300)) var=2;
 if((mouseX>150) && (mouseX<300) && (mouseY<150)) var=3;
 if((mouseX>150) && (mouseX<300) && (mouseY>150) && (mouseY<300))  var=4;
 if((mouseX<150) && (mouseY>300) && (mouseY<450)) var=5;
 if((mouseX>150) && (mouseX<300) && (mouseY>300) && (mouseY<450)) var=6;
 if((mouseX>0) && (mouseX<300) && (mouseY>450)) var=7;
 
}

// função necessária para que o vídeo seja reproduzido
void movieEvent(Movie m) {
  m.read();
}
  
  
    
