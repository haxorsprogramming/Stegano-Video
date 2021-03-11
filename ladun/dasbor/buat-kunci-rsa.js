// Route 
var rToCreateKey = server + "dashboard/proses-kunci-baru";

// Vue object 
var divMitra = new Vue({
    el : '#divMitra',
    data : {

    },
    methods : {
        buatKunciBaruAtc : function()
        {
            pesanUmumApp('success', 'Sukses', 'Berhasil membuat kunci baru ... ');
            $.post(rToCreateKey, function(data){
                divMain.titleApps = "Buat Kunci RSA";
                renderMenu("dashboard/buat-kunci-rsa");
            });
        }
    }
});

// Inisialisasi 
function pesanUmumApp(icon, title, text)
{
  Swal.fire({
    icon : icon,
    title : title,
    text : text
  });
}