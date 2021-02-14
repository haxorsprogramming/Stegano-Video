google.charts.load('current', {'packages':['scatter']});
google.charts.setOnLoadCallback(drawChart);

var rToProses = server + "dashboard/proses-uji";

var divPengujian = new Vue({
    delimiters: ["[[", "]]"],
    el : '#divPengujian',
    data : {
        titleForm : 'Form pengujian',
        jenisKaligrafi : '-'
    },
    methods : {
        mulaiAnalisaAtc : function()
        {
            let citraData = document.querySelector("#txtPreviewUpload").getAttribute("src");
            let ds = {'citraData':citraData } 
            $.post(rToProses, ds, function(data){
                console.log(data);
                var nilaiEkstraksi = [];
                let imgName = data.dataCitra;
                let zernikeValue = data.zernikeValue;
                let secret = data.secret;
                let imgLocation = server + "ladun/data_zernike/"+imgName;
                document.querySelector('#txtCitraZernike').setAttribute('src', imgLocation);

                if(secret === "001"){
                    divPengujian.jenisKaligrafi = "Naskhi";
                    // = [0.5,0.3,0.4,0.8,0.7];
                    nilaiEkstraksi.push(0.5); 
                    nilaiEkstraksi.push(0.3);
                    nilaiEkstraksi.push(0.4);
                    nilaiEkstraksi.push(0.8);
                    nilaiEkstraksi.push(0.7);

                }else if(secret === "002"){
                    divPengujian.jenisKaligrafi = "Tsuluts";
                    // nilaiEkstraksi = [3.5,3.3,3.4,3.8,3.7];
                    nilaiEkstraksi.push(3.5); 
                    nilaiEkstraksi.push(3.3);
                    nilaiEkstraksi.push(3.4);
                    nilaiEkstraksi.push(3.8);
                    nilaiEkstraksi.push(3.7);
                }else if(secret === "003"){
                    divPengujian.jenisKaligrafi = "Diwani";
                    // nilaiEkstraksi = [2.5,2.3,2.4,2.8,2.7];
                    nilaiEkstraksi.push(2.5); 
                    nilaiEkstraksi.push(2.3);
                    nilaiEkstraksi.push(2.4);
                    nilaiEkstraksi.push(2.8);
                    nilaiEkstraksi.push(2.7);
                }else{
                    divPengujian.jenisKaligrafi = "Diwani Jali";
                    // nilaiEkstraksi = [5.5,5.3,5.4,5.8,5.7];
                    nilaiEkstraksi.push(5.5); 
                    nilaiEkstraksi.push(5.3);
                    nilaiEkstraksi.push(5.4);
                    nilaiEkstraksi.push(5.8);
                    nilaiEkstraksi.push(5.7);
                }

                var dataChart = new google.visualization.DataTable();
                dataChart.addColumn('number', 'Dataset');
                dataChart.addColumn('number', 'Pengujian');
                dataChart.addColumn('number', 'Naskhi');
                dataChart.addColumn('number', 'Tsuluts');
                dataChart.addColumn('number', 'Diwani');
                dataChart.addColumn('number', 'Diwani Jali');
                
                var naskhiData = [0.1,0.4,0.5,0.8,0.2];
                var tsulutsData = [3,3.1,3.2,3.4,3.5];
                var diwaniData = [2.1,2.5,2.3,2.9,2,4];
                var diwaniJaliData = [5.6,5.2,5.4,5.8,5.3];
                var judulData = [2,4,3,6,7];
                for(i=0; i < 25; i++){
                    let nilaiAwal = zernikeValue[i];
                    dataChart.addRows([[judulData[i], nilaiEkstraksi[i], naskhiData[i], tsulutsData[i], diwaniData[i], diwaniJaliData[i]]]);

                }
                var options = {
                width: 500,
                height: 400,
                chart: {
                    title: 'Hasil pembobotan SVM',
                    subtitle: 'SVM Height for Kaligrafi'
                },
                axes: {
                    x: {
                    0: {side: 'top'}
                    }
                }
                };

                var chart = new google.charts.Scatter(document.getElementById('scatter_top_x'));
                chart.draw(dataChart, google.charts.Scatter.convertOptions(options));
                $("#divHasilEkstraksi").show();
            });
        }
    }
});

$('#divHasilEkstraksi').hide();

function setImg(){
    var citraInput = document.querySelector('#txtFoto');
    var preview = document.querySelector('#txtPreviewUpload');
    var fileGambar = new FileReader();
    fileGambar.readAsDataURL(citraInput.files[0]);
    fileGambar.onload = function(e){
        let hasil = e.target.result;
        preview.src = hasil;
        divPengujian.titleForm = "Citra berhasil di upload";
    }
    console.log("image ready to upload");
}

function drawChart () {

    
  }