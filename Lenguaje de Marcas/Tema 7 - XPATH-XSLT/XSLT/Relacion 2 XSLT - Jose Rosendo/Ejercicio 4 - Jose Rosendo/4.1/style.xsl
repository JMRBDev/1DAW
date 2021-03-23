<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>4.1 - Jose Rosendo</title>
                <style>
                    html {font-family: Arial, Helvetica, sans-serif;}
                    ul {list-style-type:none;}
                    li {color: black;}
                    li:nth-child(odd) {background-color: #2fd8a6; color: white; font-size: 18px; font-weight: bold;}
                    li:nth-child(even) {background-color: #d6d6d6; color: black; padding: 10 20; font-size: 12px; font-style: italic;}
                </style>
            </head>
            <body>
                <h1>Relación 2 XSLT - Jose Rosendo</h1>
                <h2>Ejercicio 4.1</h2>
                <xsl:for-each select="breakfast_menu/food">
                    <ul>
                        <li>
                            <xsl:value-of select="name"/>
 -                            <xsl:value-of select="price"/>
                        </li>
                        <li>
                            <xsl:value-of select="description"/>
 per serving</li>
                    </ul>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>