<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">

    <xsl:output method="xml" indent="yes"/>
    
    <xsl:variable name="statements" select="document('../CEI/CED/ELECTRIC/tariffStatements/statements_pscNbr010/XML/v.0.99.7-dev/CEI_CED_ELECTRIC_PSC10_tariff_statements_2024-12-22T1423-5.xml')"/>
    
    <!-- default identity/copy -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="/*">
        <root>
            <xsl:for-each select="//ratePlan">
                    <ratePlan><xsl:attribute name="ratePlanURI"><xsl:value-of select="@ratePlanURI"/></xsl:attribute>
                        <xsl:apply-templates/> 
                        <xsl:for-each select="$statements//statementCharges[scopeOfApplicability/include/identifiers/serviceClassReferences/serviceClassReference/serviceClassNumber = 1]">
                            <xsl:copy>
                                <xsl:apply-templates select="@*|node()"/>
                            </xsl:copy>
                        </xsl:for-each>
                    </ratePlan>
            </xsl:for-each>
        </root>
    </xsl:template>

 <!--    <xsl:template match="root/ratePlan[@ratePlanURI='https://iedr.nyserda.ny.gov/rate-plan/90d30878-b022-4c54-87bb-71fe7359aae6']"> 
    <xsl:template match="/*">
        <xsl:copy>
            <xsl:for-each select="$statements//statementCharges[scopeOfApplicability/include/identifiers/serviceClassReferences/serviceClassReference/serviceClassNumber = 1]">
                <xsl:copy>
                    <xsl:apply-templates select="@*|node()"/>
                </xsl:copy>
            </xsl:for-each>
        </xsl:copy>
    </xsl:template>
-->

</xsl:stylesheet>