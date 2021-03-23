<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>1.3 - Jose Rosendo</title>
                <style>
                    html {font-family: Arial, Helvetica, sans-serif;}
                    table, th, td {border: 2px solid black;}
                </style>
            </head>
            <body>
                <h1>Relación 2 XSLT - Jose Rosendo</h1>
                <h2>Ejercicio 1.3</h2>
                <table>
                    <tr>
                        <th>TITLE</th>
                        <th>ARTIST</th>
                        <th>COUNTRY</th>
                        <th>PRICE</th>
                        <th>YEAR</th>
                    </tr>
                    <xsl:for-each select="//CD[COUNTRY='UK']">
                        <xsl:sort select="YEAR" order="descending"/>
                        <xsl:if test="PRICE &lt; 10">
                            <xsl:if test="YEAR &lt; 2000">
                                <tr>
                                    <td>
                                        <xsl:value-of select="TITLE"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="ARTIST"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="COUNTRY"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="PRICE"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="YEAR"/>
                                    </td>
                                </tr>
                            </xsl:if>
                        </xsl:if>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>