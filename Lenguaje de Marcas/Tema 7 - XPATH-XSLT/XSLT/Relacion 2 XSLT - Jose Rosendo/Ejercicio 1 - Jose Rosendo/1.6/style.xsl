<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>1.6 - Jose Rosendo</title>
                <style>
                    html {font-family: Arial, Helvetica, sans-serif;}
                    .card{max-width: 500px; border-radius: 4px; background: #fff; box-shadow: 0 6px 10px rgba(0,0,0,.08), 0 0 6px rgba(0,0,0,.05); transition: .3s transform cubic-bezier(.155,1.105,.295,1.12),.3s box-shadow,.3s -webkit-transform cubic-bezier(.155,1.105,.295,1.12); padding: 14px 80px 18px 36px; cursor: pointer;}
                    .card:hover{transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);}
                </style>
            </head>
            <body>
                <h1>Relación 2 XSLT - Jose Rosendo</h1>
                <h2>Ejercicio 1.6</h2>
                <xsl:apply-templates select="//CD">
                    <xsl:sort select="COUNTRY"/>
                </xsl:apply-templates>
            </body>
        </html>
    </xsl:template>
    <xsl:template match="CD">
        <div class="col-md-4">
            <div class="card card-1">
                <p>
                    <xsl:apply-templates select="ARTIST"/>
                    <xsl:apply-templates select="COUNTRY"/>
                </p>
            </div>
        </div>
    </xsl:template>
    <xsl:template match="ARTIST">
        <span style="font-weight: bold; font-size:35px">ARTISTA:</span>
        <span style="color:gold; font-size:30px; font-weight:bold;">
            <xsl:value-of select="."/>
        </span>
        <br/>
    </xsl:template>
    <xsl:template match="COUNTRY">
        <span style="font-weight: bold; font-size:35px">PAÍS:</span>
        <span style="color:peru; font-size:20px">
            <xsl:value-of select="."/>
        </span>
        <br/>
    </xsl:template>
</xsl:stylesheet>