// vue object 
var divMenu = new Vue({
    delimiters: ["[[", "]]"],
    el : '#divMenu',
    data : {

    },
    methods : {
        berandaAtc : function()
        {
            divMain.titleApps = "Beranda";
            renderMenu("dashboard/beranda");
        },
        pengujianAtc : function()
        {
            divMain.titleApps = "Pengujian Encode";
            renderMenu("dashboard/pengujian");
        },
        dataKaligrafiAtc : function()
        {
            divMain.titleApps = "Data Kaligrafi";
            renderMenu("dashboard/data-kaligrafi");
        },
        buatKunciRsa : function()
        {
            divMain.titleApps = "Buat Kunci RSA";
            renderMenu("dashboard/buat-kunci-rsa");
        },
        pengujianDecodeAtc : function()
        {
            divMain.titleApps = "Pengujian Decode";
            renderMenu("dashboard/pengujian-decode");
        }
    }
});

var divMain = new Vue({
    delimiters: ["[[", "]]"],
    el : '#divMain',
    data : {
        titleApps : 'Beranda'
    },
    methods : {

    }
});


// inisialisasi & function 
divMenu.berandaAtc();

function renderMenu(halaman){
    progStart();
    $('#divUtama').html("Memuat halaman ..");
    $('#divUtama').load(server+halaman);
    progStop();
}

function progStart()
{
  NProgress.start();
}

function progStop()
{
  NProgress.done();
}