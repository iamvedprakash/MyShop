var element=''

for(let i=0;i<orders.length;i++)
{
    element+='<tr><td>'+orders[i][2]+'</td>'
    element+='<td>'+orders[i][3]+'</td>'
    element+='<td>'+orders[i][4]+'</td>'
    element+='<td>'+orders[i][6]+'</td>'
    element+='<td>'+orders[i][7]+'</td></tr>'
}



$(document).ready(function(){
    $('.order tbody').append(element)
})