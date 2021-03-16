// Route 
var rToCreateKey = server + "dashboard/proses-kunci-baru";
var rToHapusKunci = server + "dashboard/proses-hapus-kunci";

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
        },
        hapusKunciAtc : function(kdKunci)
        {
            hapusKunci(kdKunci);
        }
    }
});

// Inisialisasi 
function hapusKunci(kdKunci)
{
    let ds = {'kdKunci' : kdKunci}
    Swal.fire({
        title: "Hapus kunci?",
        text: "Jika kunci dihapus, video yang terikat dengan kunci tidak akan bisa di decode.. Yakin menghapus kunci ... ?",
        icon: "info",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Ya",
        cancelButtonText: "Tidak",
      }).then((result) => {
        if (result.value) {
           $.post(rToHapusKunci, ds, function(data){
            console.log(data);
            divMain.titleApps = "Buat Kunci RSA";
            renderMenu("dashboard/buat-kunci-rsa");
           });
        }
      });
}

function pesanUmumApp(icon, title, text)
{
  Swal.fire({
    icon : icon,
    title : title,
    text : text
  });
}

