// route 
var rToUploadVideo = server + "dashboard/pengujian/upload-video";
var rToProsesEnkripsi = server + "dashboard/pengujian/proses-enkripsi";

var kdUjiGlobal = "";
var hashFile = "";
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
            $('#frmUpload').hide();
            $('#divLoading').show();
            $('#txtPreviewUpload').hide();
        },
        success : function(data){
            console.log(data);
            let kdUji = data.kdUji;
            hashFile = data.kunci;
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
            rsa_r_1 = data.rsaF1.public;
            rsa_r_5 = data.rsaF5.public;
            rsa_r_10 = data.rsaF10.public;
            rsa_r_15 = data.rsaF15.public;
            rsa_r_20 = data.rsaF20.public;
            document.querySelector('#vRsaF1').innerHTML = rsa_r_1.substring(1, 20)+"...";
            document.querySelector('#vRsaF5').innerHTML = rsa_r_5.substring(1, 20)+"...";
            document.querySelector('#vRsaF10').innerHTML = rsa_r_10.substring(1, 20)+"...";
            document.querySelector('#vRsaF15').innerHTML = rsa_r_15.substring(1, 20)+"...";
            document.querySelector('#vRsaF20').innerHTML = rsa_r_20.substring(1, 20)+"...";

            // RSA CRT Render 
            document.querySelector('#vRsaCrtF1').innerHTML = data.rsaF1.private;
            document.querySelector('#vRsaCrtF5').innerHTML = data.rsaF5.private;
            document.querySelector('#vRsaCrtF10').innerHTML = data.rsaF10.private;
            document.querySelector('#vRsaCrtF15').innerHTML = data.rsaF15.private;
            document.querySelector('#vRsaCrtF20').innerHTML = data.rsaF20.private;

            let dataPic = data.pic_data;
            // pixel render  1
            let pix_f_1 = "<table>";
            pix_f_1 += "<tr><td> "+dataPic[0][0]+"</td><td> "+dataPic[0][1]+"</td><td> "+dataPic[0][2]+"</td></tr>";
            pix_f_1 += "<tr><td> "+dataPic[1][0]+"</td><td> "+dataPic[1][1]+"</td><td> "+dataPic[1][2]+"</td></tr>";
            pix_f_1 += "<tr><td> "+dataPic[2][0]+"</td><td> "+dataPic[2][1]+"</td><td> "+dataPic[2][2]+"</td></tr>";
            pix_f_1 += "<tr><td> "+dataPic[3][0]+"</td><td> "+dataPic[3][1]+"</td><td> "+dataPic[3][2]+"</td></tr>";
            pix_f_1 += "<tr><td> "+dataPic[4][0]+"</td><td> "+dataPic[4][1]+"</td><td> "+dataPic[4][2]+"</td></tr>";
            pix_f_1 += "</table>";
            document.querySelector("#pixF1").innerHTML = pix_f_1;

            let pix_f_5 = "<table>";
            pix_f_5 += "<tr><td> "+dataPic[5][0]+"</td><td> "+dataPic[5][1]+"</td><td> "+dataPic[5][2]+"</td></tr>";
            pix_f_5 += "<tr><td> "+dataPic[6][0]+"</td><td> "+dataPic[6][1]+"</td><td> "+dataPic[6][2]+"</td></tr>";
            pix_f_5 += "<tr><td> "+dataPic[7][0]+"</td><td> "+dataPic[7][1]+"</td><td> "+dataPic[7][2]+"</td></tr>";
            pix_f_5 += "<tr><td> "+dataPic[8][0]+"</td><td> "+dataPic[8][1]+"</td><td> "+dataPic[8][2]+"</td></tr>";
            pix_f_5 += "<tr><td> "+dataPic[9][0]+"</td><td> "+dataPic[9][1]+"</td><td> "+dataPic[9][2]+"</td></tr>";
            pix_f_5 += "</table>";
            document.querySelector("#pixF5").innerHTML = pix_f_5;

            let pix_f_10 = "<table>";
            pix_f_10 += "<tr><td> "+dataPic[10][0]+"</td><td> "+dataPic[10][1]+"</td><td> "+dataPic[10][2]+"</td></tr>";
            pix_f_10 += "<tr><td> "+dataPic[11][0]+"</td><td> "+dataPic[11][1]+"</td><td> "+dataPic[11][2]+"</td></tr>";
            pix_f_10 += "<tr><td> "+dataPic[12][0]+"</td><td> "+dataPic[12][1]+"</td><td> "+dataPic[12][2]+"</td></tr>";
            pix_f_10 += "<tr><td> "+dataPic[13][0]+"</td><td> "+dataPic[13][1]+"</td><td> "+dataPic[13][2]+"</td></tr>";
            pix_f_10 += "<tr><td> "+dataPic[14][0]+"</td><td> "+dataPic[14][1]+"</td><td> "+dataPic[14][2]+"</td></tr>";
            pix_f_10 += "</table>";
            document.querySelector("#pixF10").innerHTML = pix_f_10;

            let pix_f_15 = "<table>";
            pix_f_15 += "<tr><td> "+dataPic[15][0]+"</td><td> "+dataPic[15][1]+"</td><td> "+dataPic[15][2]+"</td></tr>";
            pix_f_15 += "<tr><td> "+dataPic[16][0]+"</td><td> "+dataPic[16][1]+"</td><td> "+dataPic[16][2]+"</td></tr>";
            pix_f_15 += "<tr><td> "+dataPic[17][0]+"</td><td> "+dataPic[17][1]+"</td><td> "+dataPic[17][2]+"</td></tr>";
            pix_f_15 += "<tr><td> "+dataPic[18][0]+"</td><td> "+dataPic[18][1]+"</td><td> "+dataPic[18][2]+"</td></tr>";
            pix_f_15 += "<tr><td> "+dataPic[19][0]+"</td><td> "+dataPic[19][1]+"</td><td> "+dataPic[19][2]+"</td></tr>";
            pix_f_15 += "</table>";
            document.querySelector("#pixF15").innerHTML = pix_f_15;

            let pix_f_20 = "<table>";
            pix_f_20 += "<tr><td> "+dataPic[20][0]+"</td><td> "+dataPic[20][1]+"</td><td> "+dataPic[20][2]+"</td></tr>";
            pix_f_20 += "<tr><td> "+dataPic[21][0]+"</td><td> "+dataPic[21][1]+"</td><td> "+dataPic[21][2]+"</td></tr>";
            pix_f_20 += "<tr><td> "+dataPic[22][0]+"</td><td> "+dataPic[22][1]+"</td><td> "+dataPic[22][2]+"</td></tr>";
            pix_f_20 += "<tr><td> "+dataPic[23][0]+"</td><td> "+dataPic[23][1]+"</td><td> "+dataPic[23][2]+"</td></tr>";
            pix_f_20 += "<tr><td> "+dataPic[24][0]+"</td><td> "+dataPic[24][1]+"</td><td> "+dataPic[24][2]+"</td></tr>";
            pix_f_20 += "</table>";
            document.querySelector("#pixF20").innerHTML = pix_f_20;


            $('#divHasilAnalisaVideo').show();
            $('#txtCapVideo').show();
            $('#txtPreviewUpload').hide();
            let imgVideoUpload = server + "ladun/data_video_upload/"+kdUji+".mp4";
            document.querySelector('#txtCapVideo').setAttribute('src', imgVideoUpload);
            pesanUmumApp('success', 'Sukses analisa', "Berhasil menganalisa video");
            $('#divStatusUji').hide();
            $('#frmUpload').hide();
            $('#divLoading').hide();
        }
    });

});

// http://127.0.0.1:7001/ladun/dasbor/img/logo_uinsu.jpg
document.querySelector('#btnEnkripsi').addEventListener('click', function(){
    let kdUji = kdUjiGlobal;
    let pesan = document.querySelector('#txtPesan').value;
    let kunci = document.querySelector('#txtKunci').value;

    let ds = {  'kdUji':kdUji, 'pesan':pesan, 'kunci':kunci, 'hashKey':hashFile}
    if(kdUji === '' || pesan === '' || kunci === ''){
        pesanUmumApp('warning', 'Isi field', 'Harap isi semua field!!!');
    }else{
        $.post(rToProsesEnkripsi, ds, function(data){
            console.log(data);
            let status_kunci = data.status_kunci;
            if(status_kunci === 'error'){
                pesanUmumApp('warning', 'Key invalid', 'Kunci RSA tidak dikenali, harap periksa kembali');
            }else{
                document.querySelector('#txtPesan').setAttribute('disabled', 'disabled');
                document.querySelector('#txtKunci').setAttribute('disabled', 'disabled');
                Swal.fire({
                    title: "Sukses?",
                    text: "Pesan berhasil disisipkan ke video, apakah ingin membuka/download video hasil pemrosesan ... ?",
                    icon: "success",
                    showCancelButton: true,
                    confirmButtonColor: "#3085d6",
                    cancelButtonColor: "#d33",
                    confirmButtonText: "Ya",
                    cancelButtonText: "Tidak",
                  }).then((result) => {
                    if (result.value) {
                        let kdUji = data.kdUji;
                        let urlVideo = server + "ladun/data_video_hash/"+kdUji+".mp4";
                        window.open(urlVideo);
                    }
                  });
                
                $('#btnEnkripsi').hide();
            }
            
        });
    }
    
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