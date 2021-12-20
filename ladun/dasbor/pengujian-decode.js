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
            let status = data.status;
            if(status === 'no_video'){
                pesanUmumApp('warning', 'No hash video', 'Video tidak memiliki data / tidak ada pesan');
            }else if(status === 'no_rsa_key'){
                pesanUmumApp('warning', 'Invalid chiper key' , 'Kode cipher tidak sesuai');
            }else{
                pesanUmumApp('success', 'Sukses', 'Pesan berhasil di encode');
                let pesan = data.pesan;
                document.querySelector("#divHasilDecode").innerHTML = '<h4>"'+pesan+'"</h4>';
                $("#divHasilDecodeVideo").show();
                console.log(pesan);
            }
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