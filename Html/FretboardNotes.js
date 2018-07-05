console.log("Connected");
notes=["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
function Notefunc()
{
    console.log(this.textContent)
    var content=this.textContent
    var note
    for (note of [7,2,10,5,0,7]){
                  var num=note
                  var i=0
                  var j=0
                  while (i<=22){
                              i=i+1

                              if(notes[num]===content)
                              {
                              data.eq(23*j+i).html(content)
                              console.log(data.eq(22*j+i).textContent)
                              console.log(content);
                            }
                              num=num+1
                              if(num>=12){
                                          num=num-12
                                        }
                              j=j+1
                              }
                }

}
data=$("td")
$("button").on("click",Notefunc);
