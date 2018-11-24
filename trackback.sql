--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Attachments; Type: TABLE; Schema: public; Owner: trackback
--

CREATE TABLE public."Attachments" (
    "Id" bigint NOT NULL,
    "MessageId" bigint,
    "Url" text,
    "Type" text
);


ALTER TABLE public."Attachments" OWNER TO trackback;

--
-- Name: Attachments_Id_seq; Type: SEQUENCE; Schema: public; Owner: trackback
--

CREATE SEQUENCE public."Attachments_Id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Attachments_Id_seq" OWNER TO trackback;

--
-- Name: Attachments_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trackback
--

ALTER SEQUENCE public."Attachments_Id_seq" OWNED BY public."Attachments"."Id";


--
-- Name: Chats; Type: TABLE; Schema: public; Owner: trackback
--

CREATE TABLE public."Chats" (
    "Id" bigint NOT NULL,
    "Topic" text,
    "IsGroup" boolean NOT NULL
);


ALTER TABLE public."Chats" OWNER TO trackback;

--
-- Name: Chats_Id_seq; Type: SEQUENCE; Schema: public; Owner: trackback
--

CREATE SEQUENCE public."Chats_Id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Chats_Id_seq" OWNER TO trackback;

--
-- Name: Chats_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trackback
--

ALTER SEQUENCE public."Chats_Id_seq" OWNED BY public."Chats"."Id";


--
-- Name: Members; Type: TABLE; Schema: public; Owner: trackback
--

CREATE TABLE public."Members" (
    "UserId" bigint NOT NULL,
    "ChatId" bigint NOT NULL,
    "UnreadedMessageCount" integer NOT NULL,
    "LastReadMessageId" bigint
);


ALTER TABLE public."Members" OWNER TO trackback;

--
-- Name: Messages; Type: TABLE; Schema: public; Owner: trackback
--

CREATE TABLE public."Messages" (
    "Id" bigint NOT NULL,
    "UserId" bigint,
    "ChatId" bigint,
    "Content" bytea,
    "Created" timestamp without time zone
);


ALTER TABLE public."Messages" OWNER TO trackback;

--
-- Name: Messages_Id_seq; Type: SEQUENCE; Schema: public; Owner: trackback
--

CREATE SEQUENCE public."Messages_Id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Messages_Id_seq" OWNER TO trackback;

--
-- Name: Messages_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trackback
--

ALTER SEQUENCE public."Messages_Id_seq" OWNED BY public."Messages"."Id";


--
-- Name: Users; Type: TABLE; Schema: public; Owner: trackback
--

CREATE TABLE public."Users" (
    "Id" bigint NOT NULL,
    "Name" text,
    "Nick" text,
    "Avatar" text
);


ALTER TABLE public."Users" OWNER TO trackback;

--
-- Name: Users_Id_seq; Type: SEQUENCE; Schema: public; Owner: trackback
--

CREATE SEQUENCE public."Users_Id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Users_Id_seq" OWNER TO trackback;

--
-- Name: Users_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trackback
--

ALTER SEQUENCE public."Users_Id_seq" OWNED BY public."Users"."Id";


--
-- Name: Attachments Id; Type: DEFAULT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Attachments" ALTER COLUMN "Id" SET DEFAULT nextval('public."Attachments_Id_seq"'::regclass);


--
-- Name: Chats Id; Type: DEFAULT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Chats" ALTER COLUMN "Id" SET DEFAULT nextval('public."Chats_Id_seq"'::regclass);


--
-- Name: Messages Id; Type: DEFAULT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Messages" ALTER COLUMN "Id" SET DEFAULT nextval('public."Messages_Id_seq"'::regclass);


--
-- Name: Users Id; Type: DEFAULT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Users" ALTER COLUMN "Id" SET DEFAULT nextval('public."Users_Id_seq"'::regclass);


--
-- Name: Attachments PK_Attachments; Type: CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Attachments"
    ADD CONSTRAINT "PK_Attachments" PRIMARY KEY ("Id");


--
-- Name: Chats PK_Chats; Type: CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Chats"
    ADD CONSTRAINT "PK_Chats" PRIMARY KEY ("Id");


--
-- Name: Members PK_Members; Type: CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Members"
    ADD CONSTRAINT "PK_Members" PRIMARY KEY ("ChatId", "UserId");


--
-- Name: Messages PK_Messages; Type: CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Messages"
    ADD CONSTRAINT "PK_Messages" PRIMARY KEY ("Id");


--
-- Name: Users PK_Users; Type: CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT "PK_Users" PRIMARY KEY ("Id");


--
-- Name: IX_Attachments_MessageId; Type: INDEX; Schema: public; Owner: trackback
--

CREATE INDEX "IX_Attachments_MessageId" ON public."Attachments" USING btree ("MessageId");


--
-- Name: IX_Members_LastReadMessageId; Type: INDEX; Schema: public; Owner: trackback
--

CREATE INDEX "IX_Members_LastReadMessageId" ON public."Members" USING btree ("LastReadMessageId");


--
-- Name: IX_Members_UserId; Type: INDEX; Schema: public; Owner: trackback
--

CREATE INDEX "IX_Members_UserId" ON public."Members" USING btree ("UserId");


--
-- Name: IX_Messages_ChatId; Type: INDEX; Schema: public; Owner: trackback
--

CREATE INDEX "IX_Messages_ChatId" ON public."Messages" USING btree ("ChatId");


--
-- Name: IX_Messages_UserId; Type: INDEX; Schema: public; Owner: trackback
--

CREATE INDEX "IX_Messages_UserId" ON public."Messages" USING btree ("UserId");


--
-- Name: Attachments FK_Attachments_Messages_MessageId; Type: FK CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Attachments"
    ADD CONSTRAINT "FK_Attachments_Messages_MessageId" FOREIGN KEY ("MessageId") REFERENCES public."Messages"("Id") ON DELETE RESTRICT;


--
-- Name: Members FK_Members_Chats_ChatId; Type: FK CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Members"
    ADD CONSTRAINT "FK_Members_Chats_ChatId" FOREIGN KEY ("ChatId") REFERENCES public."Chats"("Id") ON DELETE CASCADE;


--
-- Name: Members FK_Members_Messages_LastReadMessageId; Type: FK CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Members"
    ADD CONSTRAINT "FK_Members_Messages_LastReadMessageId" FOREIGN KEY ("LastReadMessageId") REFERENCES public."Messages"("Id") ON DELETE RESTRICT;


--
-- Name: Members FK_Members_Users_UserId; Type: FK CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Members"
    ADD CONSTRAINT "FK_Members_Users_UserId" FOREIGN KEY ("UserId") REFERENCES public."Users"("Id") ON DELETE CASCADE;


--
-- Name: Messages FK_Messages_Chats_ChatId; Type: FK CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Messages"
    ADD CONSTRAINT "FK_Messages_Chats_ChatId" FOREIGN KEY ("ChatId") REFERENCES public."Chats"("Id") ON DELETE RESTRICT;


--
-- Name: Messages FK_Messages_Users_UserId; Type: FK CONSTRAINT; Schema: public; Owner: trackback
--

ALTER TABLE ONLY public."Messages"
    ADD CONSTRAINT "FK_Messages_Users_UserId" FOREIGN KEY ("UserId") REFERENCES public."Users"("Id") ON DELETE RESTRICT;


--
-- PostgreSQL database dump complete
--

