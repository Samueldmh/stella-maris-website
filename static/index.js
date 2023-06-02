document.addEventListener("DOMContentLoaded", ()=>{
    var txt = "ABLE AND CAPABLE BY GOD'S GRACE"; /* The text */
    var i = 0
    var speed = 150; /* The speed/duration of the effect in milliseconds */
    function typewriter(){
        if (i < txt.length) {
            if (i == 16) {
                console.log(txt.charAt(i))
                line_break = document.createElement("br")
                line_break1 = document.createElement("br")
                document.querySelector("strong").appendChild(line_break)
                document.querySelector("strong").appendChild(line_break1)
            }
            else{
                document.querySelector("strong").innerHTML += txt.charAt(i);
            }
            i++;
            setTimeout(typewriter, speed);
        }    
            
    }
    typewriter()
    if (window.innerWidth < 1120  && window.innerWidth > 560){
        document.querySelector('.carousel-1').style.display = 'none';
        document.querySelector('.carousel-3').style.display = 'none';
        document.querySelectorAll('.div-content').forEach(div_content => {div_content.style.display = 'inline-block'; div_content.style.width="37.5%"; div_content.style.margin = '0 6% 0 6%'});
    }
    if (window.innerWidth < 560){
        document.querySelector('.carousel-2').style.display = 'none';
        document.querySelector('.carousel-1').style.display = 'none';
        document.querySelectorAll('.div-content').forEach(div_content => {div_content.style.display = 'inline-block'; div_content.style.width="75%"; div_content.style.margin = '0 12.5% 0 12.5%'});
    }
    if (window.innerWidth > 1120){
        document.querySelector('.carousel-3').style.display = 'none';
        document.querySelector('.carousel-2').style.display = 'none';
        document.querySelectorAll('.div-content').forEach(div_content => {div_content.style.display = 'inline-block'; div_content.style.width="25%"; div_content.style.margin = '0 4% 0 4%'});
    }
    var wtf_phone_field = document.getElementById('phone');
    console.log(wtf_phone_field)
    wtf_phone_field.style.position = 'absolute';
    wtf_phone_field.style.visibility = 'hidden';
    wtf_phone_field.style.top = '-9999px';
    wtf_phone_field.style.left = '-9999px';
    wtf_phone_field.parentElement.insertAdjacentHTML('beforeend', '<div><input type="tel" id="_phone"></div>');
})
    
            