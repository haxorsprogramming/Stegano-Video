// Route 
var rToDecode = server + "dashboard/proses-decode";

// Inisialisasi 
var divPengujianDecode = new Vue({
    delimiters: ["[[", "]]"],
    el : '#divPengujianDecode',
    data : {
        videoField : false,
        titleForm : 'Pengujian Decode'
    },
    methods : {
        analisaVideoAtc : function()
        {
            let kunciRsa = document.querySelector('#txtKunciRsa').value;
            if(kunciRsa === ''){
                pesanUmumApp('warning', 'Input Key', 'Harap input key ..');
            }else{
                $('#frmUpload').submit();
            }
        }
    }
});

$('#frmUpload').on('submit', function(e){
    e.preventDefault();
    $.ajax({
        type : 'POST',
        enctype: 'multipart/form-data',
        url : rToDecode,
        data : new FormData(this),
        contentType : false,
        cache: false,
        processData: false,
        beforeSend: function(){

        },
        success : function(data){
            console.log(data);
            let pesan = data.pesan;
            pesanUmumApp('success', 'Sukses', 'Video berhasil di decode ..');
            $('#divHasilDecodeVideo').show();
            document.querySelector('#txtKunciRsa').setAttribute("disabled", "disabled");
            $('#btnMulaiAnalisa').hide();
            document.querySelector('#divHasilDecode').innerHTML = pesan;
        }
    });

});


function detectVideo()
{
    divPengujianDecode.videoField = true;
}

function pesanUmumApp(icon, title, text)
{
  Swal.fire({
    icon : icon,
    title : title,
    text : text
  });
}