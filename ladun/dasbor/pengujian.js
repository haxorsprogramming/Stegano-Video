// route 
var rToUploadVideo = server + "dashboard/pengujian/upload-video";
// vue object 
var divPengujian = new Vue({
    delimiters: ["[[", "]]"],
    el : '#divPengujian',
    data : {
        titleForm : 'Pengujian',
        videoField : false
    },
    methods : {
        analisaVideoAtc : function()
        {
            if(this.videoField === false){
                pesanUmumApp('warning', 'Pilih video','Harap pilih video terlebih dahulu ..');
            }else{
                $("#frmUpload").submit();
            }
        }
    }
});

// inisialisasi & fungsi
$('#frmUpload').on('submit', function(e){
    e.preventDefault();
    $.ajax({
        type : 'POST',
        enctype: 'multipart/form-data',
        url : rToUploadVideo,
        data : new FormData(this),
        contentType : false,
        cache: false,
        processData: false,
        beforeSend: function(){
            $('#btnMulaiAnalisa').hide();
            $('#divStatusUji').show();
        },
        success : function(data){
            console.log(data);
            let kdUji = data.kdUji;
            let imgSrcFrame1 = server + "ladun/keras_proses/"+kdUji+"_frame_1_.jpg";
            let imgSrcFrame5 = server + "ladun/keras_proses/"+kdUji+"_frame_5_.jpg";
            let imgSrcFrame10 = server + "ladun/keras_proses/"+kdUji+"_frame_10_.jpg";
            let imgSrcFrame15 = server + "ladun/keras_proses/"+kdUji+"_frame_15_.jpg";
            let imgSrcFrame20 = server + "ladun/keras_proses/"+kdUji+"_frame_20_.jpg";
            document.querySelector('#imgFrame1').setAttribute('src', imgSrcFrame1);
            document.querySelector('#imgFrame5').setAttribute('src', imgSrcFrame5);
            document.querySelector('#imgFrame10').setAttribute('src', imgSrcFrame10);
            document.querySelector('#imgFrame15').setAttribute('src', imgSrcFrame15);
            document.querySelector('#imgFrame20').setAttribute('src', imgSrcFrame20);
            $('#divHasilAnalisaVideo').show();
        }
    });

});

// http://127.0.0.1:7001/ladun/dasbor/img/logo_uinsu.jpg

function detectVideo()
{
    divPengujian.videoField = true;
}

function pesanUmumApp(icon, title, text)
{
  Swal.fire({
    icon : icon,
    title : title,
    text : text
  });
}