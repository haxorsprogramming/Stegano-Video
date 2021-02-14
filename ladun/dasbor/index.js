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
            divMain.titleApps = "Pengujian";
            renderMenu("dashboard/pengujian");
        },
        dataKaligrafiAtc : function()
        {
            divMain.titleApps = "Data Kaligrafi";
            renderMenu("dashboard/data-kaligrafi");
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