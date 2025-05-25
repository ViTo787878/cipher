alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

def substitute_encrypt(text: str, key: str) -> str:
    if len(key) != 27 or sorted(key) != sorted(alphabet):
        raise ValueError("Klíč musí být permutace znaků A-Z a _")

    text = text.upper()
    trans_table = str.maketrans(alphabet, key)

    return text.translate(trans_table)

def substitute_decrypt(text: str, key: str) -> str:

    if len(key) != 27 or sorted(key) != sorted(alphabet):
        raise ValueError("Klíč musí být permutace znaků A-Z a _")

    text = text.upper()
    trans_table = str.maketrans(key, alphabet)

    return text.translate(trans_table)


if __name__ == "__main__":
    text_to_encrypt = "_VOZEM_DO_NEHO_A_ZAS_MNE_BEZI_DO_CESTY__ZACHVELA_SE_TAK_KUDY_VPRAVO_NEBO_VLEVO_TEDY_JE_KONEC_PTAL_SE_TISE_POKYVLA_HLAVOU_TEDY_JE_KONEC_OTEVREL_DVIRKA_VYSKOCIL_Z_VOZU_A_POSTAVIL_SE_PRED_KOLA_JED_REKL_CHRAPTIVE_POJEDES_PRESE_MNE_UJELA_S_VOZEM_DVA_KROKY_ZPET_POJD_MUSIME_DAL_DOVEZU_TE_ASPON_BLIZ_K_HRANICIM_KAM_CHCES_ZPATKY_SKRIPEL_ZUBY_ZPATKY_S_TEBOU_SE_MNOU_NENI_ANI_DOPREDU_ANI_ZPATKY_COPAK_MI_NEROZUMIS_MUSIM_TO_UDELAT_ABYS_VIDEL_ABY_BYLO_JISTO_ZE_JSEM_TE_MELA_RADA_MYSLIS_ZE_BYCH_MOHLA_JESTE_JEDNOU_SLYSET_COS_MI_REKL_ZPATKY_NEMUZES_BUD_BYS_MUSEL_VYDAT_TO_CO_NECHCES_A_NESMIS_NEBO_BY_TE_ODVEZLI_A_JA__SPUSTILA_RUCE_DO_KLINA_VIDIS_I_NA_TO_JSEM_MYSLELA_ZE_BYCH_SLA_S_TEBOU_DOPREDU_DOVEDLA_BYCH_TO_DOVEDLA_BYCH_TO_JISTE_ALE__TY_JSI_TAM_NEKDE_ZASNOUBEN_JDI_K_NI_HLED_NIKDY_ME_NENAPADLO_PTAT_SE_TE_NA_TO_KDYZ_JE_CLOVEK_PRINCEZNA_MYSLI_SI_ZE_JE_NA_SVETE_SAM_MAS_JI_RAD_POHLEDL_NA_NI_UTRYZNENYMA_OCIMA_PRECE_JEN_NEDOVEDL_ZAPRIT__TAK_VIDIS_VYDECHLA_TY_NEUMIS_ANI_LHAT_TY_MILY_ALE_POCHOP_KDYZ_JSEM_SI_TO_PAK"
    key = "VLZODTQHUXWSERMCFKNYIBJGP_A"

    encrypted = substitute_encrypt(text_to_encrypt, key)
    print(f"Original text: {text_to_encrypt}")
    print(f"Encrypted text: {encrypted}")

    decrypted = substitute_decrypt(encrypted, key)
    print(f"Decrypted text: {decrypted}")