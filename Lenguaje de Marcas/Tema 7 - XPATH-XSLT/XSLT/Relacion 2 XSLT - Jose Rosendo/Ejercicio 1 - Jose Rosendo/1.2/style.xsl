<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Catalogo de CDs</title>
                <style>html {font-family: Arial, Helvetica, sans-serif;}
                    table, th, td {border: 2px solid black;}</style>
            </head>
            <body>
                <h1>Relación 2 XSLT - Jose Rosendo</h1>
                <h2>Ejercicio 1.2</h2>
                <table>
                    <tr>
                        <th>TITLE</th>
                        <th>ARTIST</th>
                        <th>COUNTRY</th>
                        <th>PRICE</th>
                        <th>YEAR</th>
                    </tr>
                    <xsl:for-each select="//CD">
                        <tr>
                            <td>
                                <xsl:value-of select="TITLE"/>
                            </td>
                            <td>
                                <xsl:value-of select="ARTIST"/>
                            </td>
                            <xsl:choose>
                                <xsl:when test="COUNTRY = 'USA'">
                                    <td style="background-color:pink;">
                                        <xsl:value-of select="COUNTRY"/>
                                    </td>
                                </xsl:when>
                                <xsl:when test="COUNTRY = 'UK'">
                                    <td style="background-color:red;color:white;">
                                        <xsl:value-of select="COUNTRY"/>
                                    </td>
                                </xsl:when>
                                <xsl:when test="COUNTRY = 'EU'">
                                    <td style="background-color:gold;">
                                        <xsl:value-of select="COUNTRY"/>
                                    </td>
                                </xsl:when>
                                <xsl:when test="COUNTRY = 'Norway'">
                                    <td style="background-color:green;color:white;">
                                        <xsl:value-of select="COUNTRY"/>
                                    </td>
                                </xsl:when>
                                <xsl:otherwise>
                                    <td style="background-color:white;color:black;">
                                        <xsl:value-of select="COUNTRY"/>
                                    </td>
                                </xsl:otherwise>
                            </xsl:choose>
                            <td>
                                <xsl:value-of select="PRICE"/>
                            </td>
                            <td>
                                <xsl:value-of select="YEAR"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>