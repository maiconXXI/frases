async function carregarFrase(){

    const resposta = await fetch("/sortear");

    const dados = await resposta.json();

    const frase = document.getElementById("frase");

    frase.style.opacity=0;

    frase.style.transform="scale(.95)";

    setTimeout(()=>{

        frase.innerHTML=dados.texto;

        document.getElementById("autor").innerHTML="— "+dados.autor;

        frase.style.opacity=1;

        frase.style.transform="scale(1)";

    },300);

}

document
.getElementById("sortear")
.addEventListener("click",carregarFrase);

carregarFrase();

document
.getElementById("copiar")
.addEventListener("click",()=>{

    const texto=

document.getElementById("frase").innerText+

"\n"+

document.getElementById("autor").innerText;

    navigator.clipboard.writeText(texto);

    document.getElementById("mensagem").innerHTML=

"✅ Frase copiada!";

    setTimeout(()=>{

document.getElementById("mensagem").innerHTML="";

},2000);

});

document
.getElementById("compartilhar")
.addEventListener("click",async()=>{

const texto=

document.getElementById("frase").innerText+

"\n"+

document.getElementById("autor").innerText;

if(navigator.share){

await navigator.share({

title:"Frases da Vida",

text:texto

});

}else{

navigator.clipboard.writeText(texto);

document.getElementById("mensagem").innerHTML=

"Seu navegador não suporta compartilhamento. A frase foi copiada.";

setTimeout(()=>{

document.getElementById("mensagem").innerHTML="";

},3000);

}

});