<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>1.5 - Jose Rosendo</title>
                <style>
                    html {font-family: Arial, Helvetica, sans-serif;}
                    table, th, td {border: 2px solid black;}
                </style>
            </head>
            <body>
                <h1>Relación 2 XSLT - Jose Rosendo</h1>
                <h2>Ejercicio 1.5</h2>
                <ol>
                    <b>TÍTULOS:</b>
                    <xsl:for-each select="//CD">
                        <li>
                            <xsl:value-of select="TITLE"/>
                        </li>
                    </xsl:for-each>
                </ol>
                <ul>
                    <b>ARTISTAS Y AÑOS:</b>
                    <xsl:for-each select="//CD">
                        <li>
                            <xsl:value-of select="ARTIST"/>
                             - 
                            <xsl:value-of select="YEAR"/>
                        </li>
                    </xsl:for-each>
                </ul>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>