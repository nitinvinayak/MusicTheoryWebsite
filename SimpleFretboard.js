notes=["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
function Notefunc()
{
this.outerHTML=""



var note
var j=0
for (note of [7,2,10,5,0,7]){
              var num=note
              var i=0

              while (i<=22){
                          console.log(22*j+i);


                          if (data.eq(23*j+i).innerHTML==""){
                          data.eq(23*j+i).html(notes[num])
                          console.log(data.eq(22*j+i).textContent)
                        }
                          num=num+1
                          if(num>=12){
                                      num=num-12
                                    }
                          i=i+1
                          }
                          j=j+1
            }
}
$("button").on("click",Notefunc);
data=$("td")
buttons=$("button")
