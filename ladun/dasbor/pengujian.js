// route 
var rToUploadVideo = server + "dashboard/pengujian/upload-video";
var rToProsesEnkripsi = server + "dashboard/pengujian/proses-enkripsi";

var kdUjiGlobal = "";
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
$('#txtCapVideo').hide();
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
            kdUjiGlobal = kdUji;
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
            // RSA render 
            document.querySelector('#vRsaF1').innerHTML = data.rsaF1.public;
            document.querySelector('#vRsaF5').innerHTML = data.rsaF5.public;
            document.querySelector('#vRsaF10').innerHTML = data.rsaF10.public;
            document.querySelector('#vRsaF15').innerHTML = data.rsaF15.public;
            document.querySelector('#vRsaF20').innerHTML = data.rsaF20.public;

            // RSA CRT Render 
            document.querySelector('#vRsaCrtF1').innerHTML = data.rsaF1.private;
            document.querySelector('#vRsaCrtF5').innerHTML = data.rsaF5.private;
            document.querySelector('#vRsaCrtF10').innerHTML = data.rsaF10.private;
            document.querySelector('#vRsaCrtF15').innerHTML = data.rsaF15.private;
            document.querySelector('#vRsaCrtF20').innerHTML = data.rsaF20.private;
            
            $('#divHasilAnalisaVideo').show();
            $('#txtCapVideo').show();
            $('#txtPreviewUpload').hide();
            let imgVideoUpload = server + "ladun/data_video_upload/"+kdUji+".mp4";
            document.querySelector('#txtCapVideo').setAttribute('src', imgVideoUpload);
            pesanUmumApp('success', 'Sukses analisa', "Berhasil menganalisa video");
            $('#divStatusUji').hide();
            $('#frmUpload').hide();
        }
    });

});

// http://127.0.0.1:7001/ladun/dasbor/img/logo_uinsu.jpg
document.querySelector('#btnEnkripsi').addEventListener('click', function(){
    let kdUji = kdUjiGlobal;
    let pesan = document.querySelector('#txtPesan').value;
    let kunci = document.querySelector('#txtKunci').value;
    let ds = {  'kdUji':kdUji, 'pesan':pesan, 'kunci':kunci }
    $.post(rToProsesEnkripsi, function(data){
        pesanUmumApp('warning', 'Sukses', 'Pesan berhasil di sisipkan ke video');
    });
});

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